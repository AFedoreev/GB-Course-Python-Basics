# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "апельсин", "груша", "гранат", "банан"]
longest_element = len(max(fruits, key = len))  # ответ = google(вопрос)

print("Задача 1-1. Способ 1")  # без .format()
for i, fruit in enumerate(fruits, 1):  # ответ = google(вопрос)
    print(str(i) + ". " + str(fruit.rjust(longest_element, " ")))  # возможно не очень легко читается

print("\nЗадача 1-1. Способ 2")
for i, fruit in enumerate(fruits, 1):
    print('{}. {:>{}}'.format(i, fruit, longest_element))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random

print("\nЗадача 1-2.")
list_length  = 5
list1 = []
list2 = []

for _ in range(list_length):
    list1.append(random.randint(0, 10))
    list2.append(random.randint(0, 10))
print('Список 1:', list1)
print('Список 2:', list2)

kill_list = [] # пришлось делать третий лист, так как при удалении совпадения сразу после обнаружения, менялась длина
# списка и нарушался ход цикла, сброс на первую итерацию (i = 0) не помогал
for val1 in list1:
    for val2 in list2:
        if val1 == val2:
            kill_list.append(val1)

if len(kill_list) == 0:
    print('Совпадений не обнаружено')
else:
    # лист в сет для ухода от дубликатов и снова в лист для однородности отображения результатов: [] вместо {}
    print('Совпадения:', list(set(kill_list)))
    for victim in kill_list:
        list1.remove(victim)
    print('Список1 "минус" список2:', list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("\nЗадача 1-3.")
list_length  = 5
list1 = []
list2 = []

for _ in range(list_length):
    list1.append(random.randint(0, 10))
print('Список 1:', list1)

for val in list1:
    if val % 2 == 0:
        list2.append(val / 4)
    else:
        list2.append(val * 2)


print('Список 2:', list2)