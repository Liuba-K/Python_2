class Worker:

    def __init__(self, *args):
        self.name = args[0]
        self.surname = args[1]
        self.position = args[2]
        d = {}
        self._income = {"wage": d.setdefault(args[3], 300), "bonus": d.setdefault(args[4], 0)}

class Position(Worker):

    def get_full_name(self):
        print(f"{self.surname} {self.name}")

    def get_total_income(self):
        print(f"{self._income}")#нужно передать сумму

employee_1 = Position("Олег", "Пупкин", "нс", 300, 50)
employee_1.get_full_name()
employee_1.get_total_income()# не работает
