
with open("users.csv", "r", encoding="utf-8") as user:
    user_lines = []
    for line in user:
        user_lines.append(line.replace(",", " ").replace("\n", ""))
print(user_lines)

with open("hobby.csv", "r", encoding="utf-8") as hobby:
    hobby_lines = []
    for line in hobby:
        hobby_lines.append(line.replace("\n", ""))
for k, g in zip(user_lines, hobby_lines):
    print(f"{k}, {g}")


