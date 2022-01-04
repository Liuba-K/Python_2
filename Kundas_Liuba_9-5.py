class Stationery:

    def __init__(self, t):
        self.title = t

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручки")

class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандаша")

class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркера")

stationery_1 = Handle("pixar")
stationery_1.draw()
stationery_2 = Stationery("Any")
stationery_2.draw()
stationery_3 = Pen("Link")
stationery_3.draw()