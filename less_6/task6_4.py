import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        Car.move = True
        print(f'Go')

    def stop(self):
        Car.move = False
        print(f'Stop')

    def turn(self):
        if Car.move == True:
            a = ["Right", "Left", "Ahead", "Back"]
            print(f'{random.choice(a)}')
        else:
            print(f'The car is stopped')

    def show_speed(self):
        print(f'Current speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Over speed (max 60)')


class SportCar(Car):
    def color(self):
        print(f'{self.color}')
        #print(f'Current speed is {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Over speed (max 40)')


class PoliceCar(Car):
    def police(self):
        if self.is_police is True:
            print(f'It is Police car')
        else:
            print(f'It is no Police car')


tc = TownCar(70, "yellow", "Kia", False)
print(f'Town car: {tc.color} {tc.name}')
tc.go()
tc.turn()
tc.show_speed()

print('')

sc = SportCar(100, "red", "Nissan", False)
print(f'Sport car: {sc.color} {sc.name}')
sc.stop()
sc.turn()
sc.show_speed()

print('')

wc = WorkCar(50, "white", "Volvo", False)
print(f'Work car: {wc.color} {wc.name}')
wc.go()
wc.turn()
wc.show_speed()

print('')

pc = PoliceCar(120, "black", "Ford", True)
print(f'Police car: {pc.color} {pc.name}')
pc.go()
pc.turn()
pc.show_speed()
pc.police()