class Car:

    def __init__(self,s ,c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p

    def go(self):
        print(f"{self.name} go")

    def stop(self):
        print(f"{self.name} stop")

    def turn(self, direction):
        print(f"{self.name} turn {direction}")

    def show_speed(self):
        print(f"{self.name} has speed {self.speed}.")

class TownCar(Car):

    def description(self):
        print("class Town Car")

    def show_speed(self):
        if self.speed > 60:
            print("Caution. You exceeded the speed limit (60)")
        else:
            print(f"{self.name} has speed {self.speed}.")

class SportCar(Car):

    def description(self):
        print("class Sport Car")

class WorkCar(Car):

    def description(self):
        print("class Work Car")

    def show_speed(self):
        if self.speed > 40:
            print("Caution. You exceeded the speed limit (40)")
        else:
            print(f"{self.name} has speed {self.speed}.")

class PoliceCar(Car):

    def description(self):
        print("class Police Car")

Auto_1 = TownCar(100, "red", "Mazda", False)
Auto_2 = Car(20, "black", "Reno", True)
print(Auto_1.speed)
Auto_1.turn("right")
print(Auto_2.color)
Auto_2.go()
Auto_1.show_speed()
Auto_2.show_speed()
