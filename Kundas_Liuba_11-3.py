class NumberException:
    def __init__(self, *number):
        self.number = number

    def __str__(self):
        return f"\033[32m{self.number}"

number_1 = input("введите число")
res = []
try:
    for n in number_1.split():
        if n.isdigit():
            res.append(n)
        else:
            float(n)
            res.append(n)
except ValueError:
        print("Вы ввели не число")
else:
        print(f"результат", res)

#как сделать, чтобы цикл завершался input?? While