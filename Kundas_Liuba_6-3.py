from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as user:
    user_lines = []
    for line in user:
        user_lines.append(line.replace(",", " ").replace("\n", ""))
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        hobby_lines = []
        for line in hobby:
            hobby_lines.append(line.replace("\n", ""))

result = (line for line in zip_longest(user_lines, hobby_lines) if len(user_lines) > len(hobby_lines))
for line in result:
    print(line)



