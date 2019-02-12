# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random

print("\nЗадача 2-1.")
list_length = 7
list1 = []
list2 = []

for _ in range(list_length):
    list1.append(random.randint(-25, 25))

for val1 in list1:
    if val1 > 0 and (val1 ** 0.5) % 1 == 0:
        list2.append(int(val1 ** 0.5))

print('Список:', list1)
print('Список "корни":', list2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print("\nЗадача 2-2.")

days = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое',
        6: 'шестое', 7: 'седьмое', 8: 'восьмое', 9: 'девятое', 10: 'десятое', 11: 'одинадцатое', 12: 'двенадцатое',
        13: 'тринадцатое', 14: 'четырнадцатое', 15: 'пятнадцатое', 16: 'шестнадцатое', 17: 'семнадцатое',
        18: 'восемнадцатое', 19: 'девятнадцатое', 20: 'двадцатое', 21: 'двадцать первое', 22: 'двадцать второе',
        23: 'двадцать третье', 24: 'двадцать четвертое', 25: 'двадцать пятое', 26: 'двадцать шестое',
        27: 'двадцать седьмое', 28: 'двадцать восьмое', 29: 'двадцать девятое', 30: 'тридцатое', 31: 'тридцать первое'}
# сначала попробовал сделать разбить число на единицы/десятки/двадцатки и склеивать в зависимости от числа, но при
# наличии всего 31 варианта, 20 из которых уникальны, решиил не усложнять код и ввел все варианты в ручную.
# Еще понял что использовать числа для ключа в словаре, лишняя морока, и для данной задачи оптимален кортеж.
# Просто ни разу не использовал словари и решил попробовать
months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
          9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

date_list = [random.randint(1, 31), random.randint(1, 12), random.randint(0, 3000)]
print(f'{date_list[0]}.{date_list[1]}.{date_list[2]}')

# # ОПЦИЯ ДЛЯ РУЧНОГО ВВОДА ДАТЫ. Убрал чтоб при проверке ДЗ не тормозить ход программы ручным вводом
# while True:
#     date_list = input('Введите дату в формате dd.mm.yyyy: ').split('.')
#     if date_list[0].isdigit() and date_list[1].isdigit() and date_list[2].isdigit():
#         if 0 < int(date_list[0]) <= 31 and 0 < int(date_list[1]) <= 12:
#             break

day_text = days[int(date_list[0])]
month_text = months[int(date_list[1])]
print(f'{day_text} {month_text} {date_list[2]} года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print("\nЗадача 2-3.")
random_int_list = []

n = 7
for _ in range(n):
    random_int_list.append(random.randint(-100, 100))
print('Случайный список ', random_int_list)

better_option = [random.randint(-100, 100) for _ in range(n)] # В одну строку!!!

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print("\nЗадача 2-4.")
random_list = []
n = 7
for _ in range(n):
    random_list.append(random.randint(0, 5))

# с множествами быстро и удобно, но нарушает порядок элементов и не помогает в решении второй части задачи
# list_no_duplicates = list(set(random_list))

list_no_duplicates = []
list_uniq_only = []
for elem in random_list:
    if elem not in list_no_duplicates:
        list_no_duplicates.append(elem)
    if random_list.count(elem) < 2:
        list_uniq_only.append(elem)

print('Исходный список ', random_list)
print('Без повторений ', list_no_duplicates)
print('Только уникальные элементы ', list_uniq_only)
