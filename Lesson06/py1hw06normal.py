# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.hp = health
        self.dmg = damage
        self.armor = armor

    def _actual_attack(self, opponent): # инкапсуляция
        actual_attack = int(round(self.dmg / opponent.armor, 0))
        return actual_attack

    def attacks(self, opponent):
        actual_dmg = self._actual_attack(opponent) # обращение к инкапуслирванному методу в явном методе
        print(f'У {opponent.name} {opponent.hp} ХП')
        print(f'{self.name} наносит {opponent.name} урон {actual_dmg}')
        opponent.hp -= actual_dmg
        print(f'У {opponent.name} осталось {opponent.hp} ХП\n')

# как-то вышло что все атрибуты и методы остались в родительском классе и все работало без добавления уникальных методов
# в дочерние классы, поэтому стоят pass'ы, в принципе условиям задачи это не противоречит, атрибуты и классы в наличии,
# просто они все наследуются
class Player(Person):
    pass

class Enemy(Person):
    pass

class Battle:
    def __init__(self, fighter1, fighter2):
        attacker = fighter1
        while fighter1.hp > 0 and fighter2.hp > 0:
            if attacker == fighter1:
                fighter1.attacks(fighter2)
                attacker = fighter2
            else:
                fighter2.attacks(fighter1)
                attacker = fighter1

        if fighter1.hp > 0:
            print(f'{fighter1.name} победил!')
        else:
            print(f'{fighter2.name} победил!')


player = Player('Герой', 250, 75, 1.3)
enemy = Enemy('Моб', 500, 35, 1.2)
fight = Battle(player, enemy)





