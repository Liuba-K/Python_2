rus_translate = ["ноль", "один", "два", "три", "четыре",
                 "пять", "шесть", "семь", "восемь", "девять", "десять"]
eng_translate = ["zero", "one", "two", "three", "four",
                 "five", "six", "seven", "eight", "nine", "ten"]
translate = dict(zip(eng_translate, rus_translate))
""""
def num_translate(num):
    return translate[num]

print(num_translate(num))
"""


def num_translate_adv(num):
    if num[0] == num[0].title():
        return translate[num.lower()].title()
    else:
        return translate[num]


num = input("Введите число на английском от О до 10")
print(num_translate_adv(num))