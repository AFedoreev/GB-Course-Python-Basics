# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


block = 0
last_room = 0
last_floor = 0
max_room = 2000000000

target_room = ''
while not target_room.isdigit():
    target_room = input('Введите номер комнаты ')

first_room_in_block = 0
target_room = int(target_room)
if target_room >= 1 and target_room <= max_room:
    while last_room < target_room:
        first_room_in_block = last_room + 1
        last_room += block ** 2
        last_floor += block
        block += 1

    block -= 1  # откат лишнего срабатывания счетчика
    floor_within = (target_room - first_room_in_block) // block + 1  # +1 для компенсации нумерации с 0
    target_floor = last_floor - block + floor_within
    room_from_left = (target_room - first_room_in_block) % block + 1  # +1 для компенсации нумерации с 0

    print('Ваш этаж ', target_floor)
    print('Ваша комната ' + str(room_from_left) + ' слева')

else:
    print('К сожалению такой комнаты в нашей башне нет')