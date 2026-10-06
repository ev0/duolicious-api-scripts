import re

def clean_uuid_list(original_list_path, log_text_path, output_path):
    # 1. Load the original master list (UUIDs or usernames)
    with open(original_list_path, 'r', encoding='utf-8') as f:
        original_entries = [line.strip() for line in f if line.strip()]

    # 2. Load the console log text
    with open(log_text_path, 'r', encoding='utf-8') as f:
        log_text = f.read()

    # 3. Match any URL target (/UUID or /username) immediately followed by a 404 status
    pattern_404 = re.compile(
        r'duolicious\.app/([a-zA-Z0-9_-]+)\s*\[HTTP/[^\n]*?\s404\b',
        re.IGNORECASE
    )

    failed_ids = set(uid.lower() for uid in pattern_404.findall(log_text))

    # Also capture from eval console lines if present: (id) ❌ 404
    eval_pattern = re.compile(r'\(([\w-]+)\)\s*❌\s*404')
    failed_ids.update(entry.lower() for entry in eval_pattern.findall(log_text))

    # 4. Filter the list: Keep only active IDs (preserves original order)
    active_entries = [entry for entry in original_entries if entry.lower() not in failed_ids]

    # 5. Save the active list
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(active_entries))

    print("--- Filtration Summary ---")
    print(f"Total in original list:      {len(original_entries)}")
    print(f"Failed (404) IDs detected:   {len(failed_ids)}")
    print(f"Active IDs remaining:        {len(active_entries)}")
    print(f"Saved active list to '{output_path}'")

if __name__ == "__main__":
    clean_uuid_list('uuid', 'console_log.txt', 'active_uuids.txt')
