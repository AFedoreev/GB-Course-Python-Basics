# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

# Сразу приступил ко второй задаче, так как она является логическим продолжением первой

class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def procure(self):
        return str(f'Закупка сырья для производства игрушки: {self.name}')

    def sew(self):
        return str(f'Пошив игрушки: {self.name}')

    def dye(self):
        return str(f'Окраска {self.name} в {self.color} цвет')

    def produce(self):
        print(f'{self.procure()}....')
        print(f'{self.sew()}...')
        print(f'{self.dye()}..')
        print(f'Игрушка "{self.color.capitalize()} {self.name}" готова!\n')


class Animal(Toy):
    def __init__(self, name, color, toy_type='Животное'):
        super().__init__(name, color)
        self.toy_type = toy_type

    def produce(self):
        print(f'{self.procure()} ({self.toy_type})....')
        print(f'{self.sew()} ({self.toy_type})...')
        print(f'{self.dye()}..')
        print(f'Игрушка "{self.color.capitalize()} {self.name}" готова!\n')


class CartoonCharacter(Toy):
    def __init__(self, name, color, toy_type='Персонаж Мультфильма'):
        super().__init__(name, color)
        self.toy_type = toy_type

    def produce(self):
        print(f'{self.procure()} ({self.toy_type})....')
        print(f'{self.sew()} ({self.toy_type})...')
        print(f'{self.dye()}..')
        print(f'Игрушка "{self.color.capitalize()} {self.name}" готова!\n')


toy0 = Toy('Медведь', 'синий')
toy1 = Animal('Жираф', 'оранжевый')
toy2 = CartoonCharacter('Чебурашка', 'белый')

toy0.produce()
toy1.produce()
toy2.produce()
