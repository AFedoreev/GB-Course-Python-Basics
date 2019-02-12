# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

print("Задача 3-1.\n")

def attack0(attacker, beaten):
    print(f"Здоровье {beaten['name']}: {beaten['health']} ")
    beaten['health'] -= attacker['damage']
    print(f"{attacker['name']} наносит {attacker['damage']} урона сопернику {beaten['name']}")
    print(f"У {beaten['name']} осталось {beaten['health']} ХП\n")

player = {'name': 'Герой', 'health': 250, 'damage': 70}
enemy = {'name': 'Моб', 'health': 500, 'damage': 30}

# Закомментил ручной ввод для простоты тестирования
# player = {'name': input('Как зовут игрока? '), 'health': 200, 'damage': 70}
# enemy = {'name': input('Как зовут супостата? '), 'health': 500, 'damage': 30}
# attack0(player, enemy)
# attack0(enemy, player)


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

print("Задача 3-2.\n")


def damage_actual(attacker, beaten):
    final_damage = int(round(attacker['damage'] / beaten['armor'], 0)) # чтоб правильно округлять без Math
    return final_damage

def attack(attacker, beaten):
    print(f"Здоровье {beaten['name']}: {beaten['health']} ")
    beaten['health'] -= damage_actual(attacker, beaten)
    print(f"{attacker['name']} наносит {damage_actual(attacker, beaten)} урона сопернику {beaten['name']}")
    print(f"У {beaten['name']} осталось {beaten['health']} ХП\n")

def save_to_file(entity):
    filename = entity['name'] + '.txt'
    with open(filename, 'w+', encoding="UTF-8") as file:
        for key, val in entity.items():
            file.write(f'{key} / {val}\n')

def get_hero_from_file(name):
    filename = name + '.txt'
    hero_list = []
    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            hero_list.append(line.strip().split(' / '))

    for i in range(len(hero_list)):
        if hero_list[i][1].replace('.','').isdigit():
            hero_list[i][1] = float(hero_list[i][1])

    hero = dict(hero_list)
    return hero

player.update({'armor': 1.2})
enemy.update({'armor': 1.2})

save_to_file(player)
save_to_file(enemy)

player1 = get_hero_from_file('Герой')
enemy1 = get_hero_from_file('Моб')
# пришлось немного городить ветвление чтоб не было лишенго срабатывания
# (атакующий персонаж с отрицательным хп). Торопился, если честно
winner = 'никто не'
while player1['health'] > 0 and enemy1['health'] > 0:
    if player1['health'] > 0:
        attack(player1, enemy1)
    else:
        winner = enemy1['name']

    if enemy1['health'] > 0:
        attack(enemy1, player1)
    else:
        winner = player1['name']

print(f'Ура! {winner.upper()} победил!')
