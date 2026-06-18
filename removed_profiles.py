import re

def clean_uuid_list(original_list_path, log_text_path, output_path):
    with open(original_list_path, 'r', encoding='utf-8') as f:
        original_uuids = [line.strip() for line in f if line.strip()]

    with open(log_text_path, 'r', encoding='utf-8') as f:
        log_text = f.read()

    failed_pattern = re.compile(
        r'prospect-profile/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})',
        re.IGNORECASE
    )
    failed_uuids = {uid.lower() for uid in failed_pattern.findall(log_text)}

    active_uuids = [uid for uid in original_uuids if uid.lower() not in failed_uuids]

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(active_uuids))

    print("--- Filtration Summary ---")
    print(f"Total UUIDs in original list: {len(original_uuids)}")
    print(f"Failed (404) UUIDs removed: {len(failed_uuids)}")
    print(f"Active UUIDs remaining: {len(active_uuids)}")
    print(f"Saved active list to '{output_path}'")

if __name__ == "__main__":
    clean_uuid_list('original.txt', 'console_log.txt', 'active_uuids.txt')
