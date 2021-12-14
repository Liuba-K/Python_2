from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as user:
    user_lines = []
    for line in user:
        user_lines.append(line.replace(",", " ").replace("\n", ""))
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        hobby_lines = []
        for line in hobby:
            hobby_lines.append(line.replace("\n", ""))

result = {user_l: hobby_l for user_l, hobby_l in zip_longest(user_lines, hobby_lines) if
          len(user_lines) > len(hobby_lines)}
print(result)

#----------вариант 2

from itertools import zip_longest

with open("users.csv", "r", encoding="utf-8") as user:
    with open("hobby.csv", "r", encoding="utf-8") as hobby:
        result = {user_lines.replace(",", " "): hobby_lines for user_lines, hobby_lines in zip_longest(user, hobby) if len(user.readlines()) > len(hobby.readlines())}
print(result)

