
__author__ = 'Шенк Евгений Станиславович'

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
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


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
    if not file_to_copy:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_to_copy_adress = os.path.join(os.getcwd(), file_to_copy)
    new_file = str(os.path.splitext(file_to_copy)[0]+'(2)'+os.path.splitext(file_to_copy)[1])

    if os.path.isfile(file_to_copy):
        try:
            if os.path.exists(new_file):
                notEmpty = input(f'Файл {new_file} уже существует !! Перезаписать ? у :')
                if notEmpty == 'y':
                    shutil.copy(file_to_copy_adress, new_file)
                    if os.path.exists(new_file):
                        print(f'Файл {new_file} успешно перезаписан!')
                    else:
                        print('Возникли проблемы копирования !!!!!')
                else:
                    print('Файл НЕ перезаписан !')
            else:
                shutil.copy(file_to_copy_adress, new_file)
                if os.path.exists(new_file):
                    print(f'Файл {new_file} успешно создан!')
                else:
                    print("Возникли проблемы копирования !!!!!")
        except FileNotFoundError:
            print(f'Файла {file_to_copy} не существует либо ключ введен не верно (попробуйте добавить кавычки)')

    elif os.path.isdir(file_to_copy):
        try:
            if os.path.exists(new_file):
                notEmpty = input(f'Папка {new_file} уже существует !! Перезаписать ? у :')
                if notEmpty == 'y':
                    shutil.rmtree(new_file)
                    shutil.copytree(file_to_copy_adress, new_file)
                    if os.path.exists(new_file):
                        print(f'Папка {new_file} успешно перезаписана!')
                    else:
                        print('Возникли проблемы копирования !!!!!')
                else:
                    print('Папка НЕ перезаписана !')
            else:
                shutil.copytree(file_to_copy_adress, new_file)
                if os.path.exists(new_file):
                    print(f'Папка {new_file} успешно создана!')
                else:
                    print("Возникли проблемы копирования !!!!!")
        except FileNotFoundError:
            print(f'Файла {file_to_copy} не существует либо ключ введен не верно (попробуйте добавить кавычки)')

    else:
        print(f'{file_to_copy} не существует либо ключ введен не верно (попробуйте добавить кавычки)')


def remove_file():
    if not file_to_delete:
        print("Необходимо указать имя файла вторым параметром")
        return

    if os.path.isfile(file_to_delete):
        conf_to_del = input(f'Удалить файл {file_to_delete} ? у :')
        if conf_to_del == 'y':
            os.remove(file_to_delete)
            if not os.path.exists(file_to_delete):
                print(f'Файл {file_to_delete} успешно удален!')
            else:
                print('Возникли проблемы при удалении !!!!!')
        else:
            print(f'Удаление файла {file_to_delete} отменено !')

    elif os.path.isdir(file_to_delete):
        conf_to_del = input(f'Удалить папку {file_to_delete} ? у :')
        if conf_to_del == 'y':
            try:
                os.rmdir(file_to_delete)
            except OSError:
                notEmpty = input(f'Папка {file_to_delete} не пуста !! Удалить ? y : ')
                if notEmpty == 'y':
                    shutil.rmtree(file_to_delete)
                    print(f'Папка {file_to_delete} успешно удалена!')
                else:
                    print(f'Удаление папки {file_to_delete} отменено !!')
        else:
            print(f'Удаление папки {file_to_delete} отменено !!')

    else:
        print(f'{file_to_delete} не существует либо ключ введен не верно (попробуйте добавить кавычки)')


def change_dir():
    if not dir_to_go:
        print("Необходимо указать имя директории вторым параметром")
        return
    try:
        os.chdir(dir_to_go)
    except FileNotFoundError:
        print('Невозможно перейти, такой папки не существует')
    else:
        print('Текущая директория успешно изменена на:')
        show_full_path()


def show_full_path():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": show_full_path,
    }

try:
    dir_name = sys.argv[2]
    file_to_copy = sys.argv[2]
    file_to_delete = sys.argv[2]
    dir_to_go = sys.argv[2]
except IndexError:
    dir_name = None
    file_to_copy = None
    file_to_delete = None
    dir_to_go = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
