class Road:

    def __init__(self, l, w):
        self._lenght = l
        self._width = w

    def calcul_asphalt(self):
        res = self._width * self._lenght * 25 * 5 / 1000
        print(f"{res} т")

a = Road(20, 5000)
a.calcul_asphalt()
