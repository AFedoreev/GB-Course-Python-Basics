# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import re
import shutil


def create_dir(string):
    arg_list = string.split(' ')
    if len(arg_list) == 1: # на случай если пользователь введет только имя папки, без количества папок
        dir_name = arg_list[0]
        n = 1
    elif len(arg_list) == 2:
        dir_name, n = arg_list
    else:
        print('Неверный ввод!')
        return

    for i in range(1, int(n) + 1):
        if int(n) != 1:
            fullpath = os.path.join(os.getcwd(), dir_name + str(i)) # возможно рациональней присвоить getcwd переменной
            # один раз перед циклом чтоб каждый раз ее не запускать
        else:
            fullpath = os.path.join(os.getcwd(), dir_name) # в случае ввода количества файлов 1, номер не включается

        if not os.path.exists(fullpath):
            os.mkdir(fullpath)
            print(f'Создана папка {os.path.basename(fullpath)}')
        else:
            print(f'Папка {os.path.basename(fullpath)} уже существует!')


def del_dir(dir_prefix):
    dir_count = 0 # пришлось вводить счетчик на случай если не найдется папок согласно маске, иначе были ложные
    # срабатывания для сообщения что папки не найдены
    while True:
        user_confirm = input(f'Вы точно хотите удалить все папки начинающиеся с "{dir_prefix}" (Y/N)? ').upper()
        if user_confirm == 'Y':
            for dir in os.listdir(os.getcwd()):
                if os.path.isdir(dir) and re.match(f'^({dir_prefix})', dir):
                    dir_count += 1
                    user_confirm = input(f'Вы точно хотите удалить "{dir}" (Y/N)? ').upper() # лучше перестраховаться :)
                    if user_confirm == 'Y':
                        try:
                            # os.remove()  # PermissionError: [WinError 5] Access is denied: 'dir_1'. Может не тот
                            # метод. Но запускаю на рабочем компе, на котором иногда возникают проблемы с админ правами,
                            # если верить гуглу, то возможно в этом причина проблем с удалением папок, файлы удаляются
                            # без проблем. И если удалять папки через обычный интерфейс винды, тоже все норм.
                            os.rmdir(os.path.join(os.getcwd(), dir)) # в отличие от remove() - работает
                            print(f'Папка {dir} успешно удалена!')
                        except:
                            print('Ошибка удаления!')
            if dir_count == 0:
                print('Таких папок не найдено!')
            break
        elif user_confirm == 'N':
            print('Фуф! Я чего-то тож не очень уверен был!')
            break
        else:
            print('Пожалуйста произносите отчетливей: Y или N? ')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dirs_only():
    for file in os.listdir(os.getcwd()):
        if os.path.isdir(file): #  согласно задания, отображаю только папки, не файлы, поэтому не использовал эту
            # функцию в нормале
            print(file)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def dupl_itself(fullpath):
    newfilename = os.path.join(os.getcwd(), 'Сopy of ' + os.path.basename(fullpath))
    if not os.path.exists(newfilename):
        shutil.copy(str(fullpath), newfilename) # Знаю только через shutil, проходили на интенсиве кажется
    else:
        user_confirm = input('Такой файл уже существует, хотите его заменить? (Y/N) ')
        if user_confirm == 'Y':
            shutil.copy(str(fullpath), newfilename)


if __name__ == '__main__':
    #create_dir('dir_', 9)
    #del_dir('dir_')
    list_dirs_only()
    #dupl_itself(__file__)