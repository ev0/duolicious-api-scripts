import asyncio
import string
import itertools
import time
import json
import os
import aiohttp
import argparse

API_URL = "https://api.duolicious.app/search-public-clubs"

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://example.com",
    "Referer": "https://example.com/",
    "Sec-Ch-UA": '"Not-A.Brand";v="24", "Chromium";v="146"',
    "Sec-Ch-UA-Mobile": "?1",
    "Sec-Ch-UA-Platform": '"Android"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36"
}

REQUESTS_PER_MINUTE = 55
RATE_LIMIT_PAUSE = 60

CRAWL_CHARS = string.ascii_lowercase + string.digits + "'\"" + " !@#$%^&*()-_=+[]{}|;:,./<>?~`\\"


class AsyncRateLimiter:
    def __init__(self, rpm):
        self.delay = 60.0 / rpm
        self.last_called = 0.0

    async def wait(self):
        now = time.monotonic()
        elapsed = now - self.last_called
        if elapsed < self.delay:
            await asyncio.sleep(self.delay - elapsed)
        self.last_called = time.monotonic()


def load_state(state_file):
    """Loads previous crawl state if it exists."""
    if os.path.exists(state_file):
        try:
            with open(state_file, "r", encoding="utf-8") as f:
                state = json.load(f)
                completed = state.get("completed_prefixes", [])
                clubs = state.get("unique_clubs", {})
                print(f"-> Found existing checkpoint ({state_file}). Loaded {len(clubs):,} unique clubs.")
                return completed, clubs
        except Exception as e:
            print(f"Error loading checkpoint file ({e}). Starting fresh.")
    return [], {}


def save_state(state_file, completed_prefixes, unique_clubs):
    """Saves the current crawl progress and unique clubs to a JSON file."""
    state = {
        "completed_prefixes": completed_prefixes,
        "unique_clubs": unique_clubs
    }
    try:
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4)
    except Exception as e:
        print(f"Error saving checkpoint state to {state_file}: {e}")


def get_member_count(club_obj):
    return club_obj.get("count_members", 0)


def print_top_clubs(unique_clubs, completed_prefixes, total_stages=None):
    """Sorts and displays the top 100 clubs found so far."""
    sorted_clubs = sorted(
        unique_clubs.values(),
        key=get_member_count,
        reverse=True
    )
    progress_str = f"{len(completed_prefixes)} stages completed"
    if total_stages:
        progress_str = f"{len(completed_prefixes)} / {total_stages} stages completed"

    print("\n" + "=" * 55)
    print(f"   CURRENT TOP 100 CLUBS FOUND SO FAR ({progress_str})")
    print("=" * 55)
    for idx, club in enumerate(sorted_clubs[:100], 1):
        name = club.get("name", "Unknown")
        members = get_member_count(club)
        print(f"{idx:03d}. {name:<35} ({members:,} members)")
    print("=" * 55 + "\n")


async def main(length):
    limiter = AsyncRateLimiter(REQUESTS_PER_MINUTE)

    # Separate checkpoint file based on the query length argument
    state_file = f"clubs_progress_len{length}.json"

    # Build the specific stages required for the requested query length
    stages = []

    if length == 1:
        stages.append({
            "key": "len_1",
            "display": "Phase 1: 1-character queries",
            "queries": [char for char in CRAWL_CHARS]
        })

    elif length == 2:
        for char in CRAWL_CHARS:
            stages.append({
                "key": f"len_2_{char}",
                "display": f"Phase 2: 2-character queries starting with {repr(char)}",
                "queries": [char + suffix for suffix in CRAWL_CHARS]
            })

    elif length == 3:
        for char in CRAWL_CHARS:
            stages.append({
                "key": f"len_3_{char}",
                "display": f"Phase 3: 3-character queries starting with {repr(char)}",
                "queries": [char + "".join(suffix) for suffix in itertools.product(CRAWL_CHARS, repeat=2)]
            })

    total_stages = len(stages)
    total_queries = sum(len(s["queries"]) for s in stages)

    # Load checkpoint for this specific length
    completed_prefixes, unique_clubs = load_state(state_file)

    print(f"--- Crawl Configured for {length}-character queries ---")
    print(f"Pacing requests at ~{REQUESTS_PER_MINUTE} RPM (one request every {60.0 / REQUESTS_PER_MINUTE:.2f}s).")
    print(f"Total Stages: {total_stages} | Total Queries to Run: {total_queries:,}")
    print(f"Targeting state file: {state_file}")
    print("Press Ctrl+C to stop. Your progress will be saved.")

    async with aiohttp.ClientSession() as session:
        for stage in stages:
            stage_key = stage["key"]
            if stage_key in completed_prefixes:
                continue

            queries = stage["queries"]
            print(f"\n--- Starting: {stage['display']} ({len(queries)} queries) ---")

            idx = 0
            retries = 0
            max_retries = 3

            while idx < len(queries):
                query = queries[idx]
                await limiter.wait()

                params = {"q": query}
                try:
                    async with session.get(API_URL, params=params, headers=HEADERS, timeout=10) as response:

                        if response.status == 200:
                            results = await response.json()

                            if isinstance(results, list):
                                for club in results:
                                    club_name = club.get("name")
                                    if club_name and club_name not in unique_clubs:
                                        unique_clubs[club_name] = club
                            else:
                                print(f"Received unexpected non-list JSON response for query {repr(query)}")

                            idx += 1
                            retries = 0  # Reset retries on success

                        elif response.status == 429:
                            print(
                                f"\n[HTTP 429] Rate limit hit on query {repr(query)}. Pausing for {RATE_LIMIT_PAUSE} seconds...")
                            await asyncio.sleep(RATE_LIMIT_PAUSE)

                        else:
                            retries += 1
                            if retries >= max_retries:
                                print(
                                    f"Query {repr(query)} failed with status {response.status} after {max_retries} attempts. Skipping.")
                                idx += 1
                                retries = 0
                            else:
                                print(
                                    f"Query {repr(query)} failed with status {response.status}. Retrying ({retries}/{max_retries}) in 5 seconds...")
                                await asyncio.sleep(5)

                except Exception as e:
                    retries += 1
                    if retries >= max_retries:
                        print(f"Error on query {repr(query)} after {max_retries} attempts: {e}. Skipping.")
                        idx += 1
                        retries = 0
                    else:
                        print(f"Error on query {repr(query)}: {e}. Retrying ({retries}/{max_retries}) in 5 seconds...")
                        await asyncio.sleep(5)

            completed_prefixes.append(stage_key)
            save_state(state_file, completed_prefixes, unique_clubs)
            print_top_clubs(unique_clubs, completed_prefixes, total_stages)

    print(f"\nCrawl complete! All stages for length {length} have been processed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Duolicious Club Crawler")
    parser.add_argument(
        "length",
        type=int,
        choices=[1, 2, 3],
        nargs="?",
        default=1,
        help="Length of combinations to search (1, 2, or 3). Default is 1."
    )
    args = parser.parse_args()

    try:
        asyncio.run(main(args.length))
    except KeyboardInterrupt:
        print("\nCrawl interrupted by user. Progress saved.")
