import json
import os

OUTPUT_FILE = "clubs_progress.json"
INPUT_FILES = [
    "clubs_progress_len1.json",
    "clubs_progress_len2.json",
    "clubs_progress_len3.json"
]


def merge_and_display():
    combined_completed_prefixes = []
    combined_unique_clubs = {}

    # 1. Load and merge the available JSON files
    for file_name in INPUT_FILES:
        if os.path.exists(file_name):
            print(f"Reading {file_name}...")
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    state = json.load(f)

                    # Merge the list of completed prefixes
                    prefixes = state.get("completed_prefixes", [])
                    combined_completed_prefixes.extend(prefixes)

                    # Merge unique clubs
                    clubs = state.get("unique_clubs", {})
                    for club_name, club_obj in clubs.items():
                        # If a duplicate name is found, keep the one with the highest member count
                        if club_name in combined_unique_clubs:
                            current_count = combined_unique_clubs[club_name].get("count_members", 0)
                            new_count = club_obj.get("count_members", 0)
                            if new_count > current_count:
                                combined_unique_clubs[club_name] = club_obj
                        else:
                            combined_unique_clubs[club_name] = club_obj
            except Exception as e:
                print(f"Error reading {file_name}: {e}")
        else:
            print(f"Notice: {file_name} not found in this directory. Skipping.")

    if not combined_unique_clubs:
        print("Error: No data found to combine.")
        return

    # 2. Save combined state to the unified file
    combined_state = {
        "completed_prefixes": combined_completed_prefixes,
        "unique_clubs": combined_unique_clubs
    }

    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(combined_state, f, indent=4)
        print(f"Successfully combined and saved {len(combined_unique_clubs):,} total unique clubs to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error saving combined state: {e}")
        return

    # 3. Sort and print the top 100 collected clubs
    def get_member_count(club_obj):
        return club_obj.get("count_members", 0)

    sorted_clubs = sorted(
        combined_unique_clubs.values(),
        key=get_member_count,
        reverse=True
    )

    print("\n" + "=" * 55)
    print(f"      TOP 100 COMBINED CLUBS COLLECTED ({len(combined_unique_clubs):,} total)")
    print("=" * 55)

    for idx, club in enumerate(sorted_clubs[:100], 1):
        name = club.get("name", "Unknown")
        members = get_member_count(club)
        print(f"{idx:03d}. {name:<35} ({members:,} members)")

    print("=" * 55 + "\n")


if __name__ == "__main__":
    merge_and_display()
