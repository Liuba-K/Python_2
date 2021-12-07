
def odd_to_15(n):
    for odd_nums in range(1, n + 1, 2):
        yield odd_nums

n = int(input("Введите число, до которого будут генерироваться нечетные числа"))

for i in odd_to_15(n):
    print(i)

# ____________task_5-2
n = int(input("Введите число, до которого будут генерироваться нечетные числа"))

odd_to_15 = (odd_nums for odd_nums in range(1, n + 1, 2))
for number in odd_to_15:
    print(number)

