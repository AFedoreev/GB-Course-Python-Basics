# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil
import re
print('sys.argv = ', sys.argv)

# На кроссплатформу не хватило времени, но немного погуглил, смысл ясен, разные функции, пути в зависимости от системы
# Обязательно попробую позже
# if sys.platform == "Windows":
#     os.system("md " + dir_name)
# elif sys.platform == "Linux":
#     os.system("mkdir " + dir_name)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy_file():
    if not file_name:
        print('Вторым параметром необходимо указать имя файла для копирования')
        return
    file_path = os.path.join(os.getcwd(), file_name)
    new_name = 'Copy of ' + file_name
    try:
        if not os.path.exists(os.path.join(os.getcwd(), new_name)):
            shutil.copy(file_path, new_name)
            print(f'Файл {file_name} скопирован')
        else:
            user_confirm = input(f'Копия файла {file_name} уже есть, хотите заменить его? (Y/N)')
            if user_confirm.upper() == 'Y':
                shutil.copy(file_path, new_name)
                print(f'Новая копия файла {file_name} заменила старую')
            else:
                print('Нет так нет')
                return
    except FileNotFoundError:
        print("Файл для копирования не найден!")


def remove_file():
    if not file_name:
        print('Вторым параметром необходимо указать имя файла для удаления')
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        user_confirm = input(f'Вы точно хотите удалить "{file_name}" (Y/N) ')
        if user_is_sure(user_confirm):
            os.remove(file_path)
            print(f'Файл {file_name} удален!')
    except FileNotFoundError:
        print("Файл для удаления не найден!")


def dir_change():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print(f'Вы перешли в {os.getcwd()}')  # папку меняет, но после отработки, коммандная строка снова переходит в старую папку
    except FileNotFoundError:
        print('Директория для перехода не найдена!')


def get_path():
    print(f'Текущая директория: {os.getcwd()}')


def user_is_sure(user_entry):
    if re.match('Y|y|yes|Yes|Да|да|Нуы|нуы', user_entry):
        return True
    else:
        return False


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": dir_change,
    "ls": get_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
