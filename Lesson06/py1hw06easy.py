# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar0:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала и разогналась до {self.speed} км/ч')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')


class SportCar0:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала и разогналась до {self.speed} км/ч')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')


class WorkCar0:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала и разогналась до {self.speed} км/ч')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')


class PoliceCar0:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала и разогналась до {self.speed} км/ч')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')



# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} поехала и разогналась до {self.speed} км/ч')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')

#  Разница между классами в первом задании только в том являются они полицией или нет, остальное общее ушло к родителю
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)  # 3 атрибута от родителя
        self.is_police = is_police # 1 свой

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)  # 3 атрибута от родителя
        self.is_police = is_police # 1 свой

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)  # 3 атрибута от родителя
        self.is_police = is_police # 1 свой

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)  # 3 атрибута от родителя
        self.is_police = is_police # 1 свой

towncar1 = TownCar(80, 'white', 'Camry', False)
sportcar1 = SportCar(200, 'yellow', 'Lambo', False)
workcar1 = WorkCar(60, 'black', 'Land Cruiser', False)
policecar1 = PoliceCar(200, 'blue', 'Charger', True)

# провека на работоспособность
towncar1.turn('налево')
towncar1.go()
towncar1.stop()

sportcar1.turn('направо')
sportcar1.go()
sportcar1.stop()