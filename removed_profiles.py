uuid=pass

uuid_example="""ff618e0e-94d7-4894-80b7-9a426f17822b
ff61b25d-9a4c-4c19-9786-a18c4e4cb181"""

log_text_example="""VM37:98 [1/6564] ❌ 404
VM37:98 [2/6564] ❌ 404"""

log_text = pass

# you need to fill these in yourself, uuids are in the repository,
# but the log_text to be up to date needs to be fetched yourself.

def fix_list(uuid_list, log_text):
    indices = re.findall(r'\[(\d+)/', log_text)
    indices = sorted([int(i) for i in indices], reverse=True)
    for idx in indices:
        try:
            uuid_list.pop(idx - 1)
        except IndexError:
            pass
    return uuid_list

uuid_as_list = uuid.splitlines()
cleaned_list = fix_list(uuid_as_list, input_removed)

result_string = "\n".join(cleaned_list)
print(result_string)
