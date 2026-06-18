import json
import os

STATE_FILE = "clubs_progress.json"


def print_current_top_100():
    if not os.path.exists(STATE_FILE):
        print(f"Error: {STATE_FILE} not found in this directory.")
        return

    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)

        unique_clubs = state.get("unique_clubs", {})
        completed_prefixes = state.get("completed_prefixes", [])

        if not unique_clubs:
            print("No clubs found in the progress file.")
            return

        # Helper to get the member count safely
        def get_member_count(club_obj):
            return club_obj.get("count_members", 0)

        # Sort the collected clubs descending by member count
        sorted_clubs = sorted(
            unique_clubs.values(),
            key=get_member_count,
            reverse=True
        )

        completed_str = ", ".join(completed_prefixes).upper() if completed_prefixes else "None"

        # Display header and stats
        print("\n" + "=" * 55)
        print(f"      TOP 100 CLUBS COLLECTED SO FAR ({len(unique_clubs):,} total)")
        print(f"      Completed starting letters: {completed_str}")
        print("=" * 55)

        # Print up to the top 100 clubs
        for idx, club in enumerate(sorted_clubs[:100], 1):
            name = club.get("name", "Unknown")
            members = get_member_count(club)
            print(f"{idx:03d}. {name:<35} ({members:,} members)")

        print("=" * 55 + "\n")

    except Exception as e:
        print(f"An error occurred reading the file: {e}")


if __name__ == "__main__":
    print_current_top_100()
