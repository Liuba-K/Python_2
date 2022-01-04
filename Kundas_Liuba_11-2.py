class ZeroException:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"\033[32m{self.number}"

    def __truediv__(self, other):
        return ZeroException(self.number / other.number)

number_1 = ZeroException(int(input("введите число")))
number_2 = ZeroException(int(input("введите число")))

try:
    res = number_1 / number_2
except ZeroDivisionError:
    print("Вы разделили на ноль")
else:
    print(f"результат {res}")

