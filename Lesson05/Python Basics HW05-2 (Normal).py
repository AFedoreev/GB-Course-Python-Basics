# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import hw05easy as easy

def dir_change():
    try:
        print('Текущая директория:', os.getcwd())
        dir_path = input('Введите имя папку куда хотите перейти: ')
        os.chdir(os.path.join(os.getcwd(), dir_path))
        print('Успешно перешли в : ', os.getcwd())
    except FileNotFoundError:
        print('Директория для перехода не найдена!')

# провел только частичный отлов багов, на полный не было времени, но при относительной адекватности пользователя работает

def start():
    user_entry = ''
    while user_entry != 'Q' or user_entry != 'q':
        print('\nВыберите действие:\n'
              '[1] - Перейти в папку\n'
              '[2] - Просмотреть содержимое текущей папки\n'
              '[3] - Удалить папку/папки\n'
              '[4] - Создать папку/папки\n'
              '[Q] - Выйти')
        user_entry = input()

        if user_entry == '1':
            dir_change()

        elif user_entry == '2':
            print(f'Папка "{os.path.basename(os.getcwd())}" содержит: ')
            for file in os.listdir():
                print(file)

        elif user_entry == '3':
            prefix = input('Введите префикс имени папок которые хотите удалить: ')
            easy.del_dir(prefix)

        elif user_entry == '4':
            user_entry =  input('Введите префикс с которого будут начинаться имена папок и количество папок '
                                 '(через пробел): ')
            easy.create_dir(user_entry)
        else:
            return # выход на любой другой символ, не только Q

start()