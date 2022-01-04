import time

class TrafficLight:

    def __init__(self):
        self.__color = ("красный", "желтый", "зеленый")

    def running(self, n):

        for d in range(n):
            for i in self.__color:
                if i == "красный":
                    time.sleep(7)
                elif i == "желтый":
                    time.sleep(2)
                elif i == "зеленый":
                    time.sleep(5)
                print(i)

a = TrafficLight()
a.running(2)


