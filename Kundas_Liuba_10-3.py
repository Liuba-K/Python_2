class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f"\033[32m{self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(self.cell // other.cell)

    def __truediv__(self, other):
        return Cell(self.cell / other.cell)

    def make_order(self, row):
        pass

cell_1 = Cell(13)
cell_2 = Cell(12)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(5))
