class ComplexNumber:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"\033[30m{self.date}"

    def __add__(self, other):
        return ComplexNumber(self.date + other.date)

    def __mul__(self, other):
        return ComplexNumber(self.date * other.date)

com_1 = ComplexNumber(complex(4, 3))
com_2 = ComplexNumber(complex(2, 1))

print(com_1 + com_2)
print(com_1 * com_2)
