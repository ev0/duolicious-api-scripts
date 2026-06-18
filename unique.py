# 1. Read the lines from the file
with open("uuid", "r") as f:
    lines = f.read().splitlines()

# 2. Convert to dict keys to remove duplicates instantly while keeping order
unique_list = list(dict.fromkeys(lines))

# 3. Print each item on a new line (OUTSIDE the loops)
for item in unique_list:
    print(item)
