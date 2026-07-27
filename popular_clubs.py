import asyncio
import string
import itertools
import time
import json
import os
import aiohttp

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
STATE_FILE = "clubs_progress.json"


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


def load_state():
    """Loads previous crawl state if it exists."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
                completed = state.get("completed_prefixes", [])
                clubs = state.get("unique_clubs", {})
                print(
                    f"-> Found existing checkpoint. Letters already completed: {', '.join(completed) if completed else 'None'}")
                return completed, clubs
        except Exception as e:
            print(f"Error loading checkpoint file ({e}). Starting fresh.")
    return [], {}


def save_state(completed_prefixes, unique_clubs):
    """Saves the current crawl progress and unique clubs to a JSON file."""
    state = {
        "completed_prefixes": completed_prefixes,
        "unique_clubs": unique_clubs
    }
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4)
    except Exception as e:
        print(f"Error saving checkpoint state: {e}")


def get_member_count(club_obj):
    return club_obj.get("count_members", 0)


def print_top_clubs(unique_clubs, completed_prefixes):
    """Sorts and displays the top 100 clubs found so far."""
    sorted_clubs = sorted(
        unique_clubs.values(),
        key=get_member_count,
        reverse=True
    )
    completed_str = ", ".join(completed_prefixes) if completed_prefixes else "None"
    print("\n" + "=" * 55)
    print(f"   CURRENT TOP 100 CLUBS FOUND SO FAR (Completed: {completed_str})")
    print("=" * 55)
    for idx, club in enumerate(sorted_clubs[:100], 1):
        name = club.get("name", "Unknown")
        members = get_member_count(club)
        print(f"{idx:03d}. {name:<35} ({members:,} members)")
    print("=" * 55 + "\n")

async def main():
    alphabet = string.ascii_lowercase
    limiter = AsyncRateLimiter(REQUESTS_PER_MINUTE)

    completed_prefixes, unique_clubs = load_state()

    print(f"Pacing requests at ~{REQUESTS_PER_MINUTE} RPM (one request every {60.0 / REQUESTS_PER_MINUTE:.2f}s).")
    print("Press Ctrl+C to stop. Your progress will be saved.")

    async with aiohttp.ClientSession() as session:
        for prefix in alphabet:
            if prefix in completed_prefixes:
                continue

            suffixes = ["".join(combo) for combo in itertools.product(alphabet, repeat=2)]
            queries = [prefix + suffix for suffix in suffixes]

            print(f"\n--- Starting Crawl for Letter '{prefix.upper()}' ({len(queries)} queries) ---")
            idx = 0

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
                                print(f"Received unexpected non-list JSON response for query '{query}'")

                            idx += 1

                        elif response.status == 429:
                            print(
                                f"\n[HTTP 429] Rate limit hit on query '{query}'. Pausing for {RATE_LIMIT_PAUSE} seconds...")
                            await asyncio.sleep(RATE_LIMIT_PAUSE)

                        else:
                            print(f"Query '{query}' failed with status {response.status}. Retrying in 5 seconds...")
                            await asyncio.sleep(5)

                except aiohttp.ContentTypeError:
                    print(f"Error: Non-JSON response received for query '{query}'. Retrying in 5 seconds...")
                    await asyncio.sleep(5)
                except Exception as e:
                    print(f"Network error on query '{query}': {e}. Retrying in 5 seconds...")
                    await asyncio.sleep(5)

            completed_prefixes.append(prefix)
            save_state(completed_prefixes, unique_clubs)
            print_top_clubs(unique_clubs, completed_prefixes)

    print("\nCrawl complete! All letters 'a' through 'z' have been processed.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nCrawl interrupted by user. Progress saved.")
