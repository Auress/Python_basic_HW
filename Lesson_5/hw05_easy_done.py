
__author__ = 'Шенк Евгений Станиславович'

import sys
import os
import shutil


def create_dir(dir_name):       # Task_1
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print(f'>>> <<<\nПапка {dir_name} уже существует !!\n>>> <<<')
    else:
        print(f'>>> <<<\nПапка {dir_name} успешно создана!\n>>> <<<')


def delete_dir(dir_name):       # Task_1
    try:
        os.rmdir(dir_name)
    except FileNotFoundError:
        print(f'>>> <<<\nПапки {dir_name} не существует !!\n>>> <<<')
    except OSError:
        notEmpty = input(f'Папка {dir_name} не пуста !! Удалить ? y : ')
        if notEmpty == 'y':
            shutil.rmtree(dir_name)
            print(f'>>> <<<\nПапка {dir_name} успешно удалена!\n>>> <<<')
        else:
            print(f'>>> <<<\nУдаление папки {dir_name} отменено !!\n>>> <<<')


def cur_path_dir():        # Task_2
    print('Список папок в текущей директории :')
    print(sorted([x for x in os.listdir('.') if os.path.isdir(x)]))
    print('>>> <<<')


if __name__ == "__main__":
    while True:
        task = input('Введите номер решаемой задачи (1, 2, 3, q) : ')

    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.

        if task == '1':
            while True:
                task = input('Создать папки / удалить папки / выйти из скрипта: c / d / q : ')
                i = 1
                n = 9
                if task == 'c' or task == 'd':
                    while True:
                        try:
                            i = int(input('Укажите начальный номер папки: '))
                            n = int(input('Укажите конечный номер папки: '))
                        except ValueError:
                            print('Номера должны иметь целочисленные значения !!')
                        else:
                            if i > n:
                                i, n = n, i
                            break

                if task == 'c':
                    while i <= n:
                        name = f'dir_{i}'
                        create_dir(name)
                        i += 1

                if task == 'd':
                    while i <= n:
                        name = f'dir_{i}'
                        delete_dir(name)
                        i += 1

                if task == 'q':
                    break


    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

        if task == '2':
            cur_path_dir()


    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

        if task == '3':
            file_to_copy = sys.argv[0]
            new_file = file_to_copy + '.dupl'
            if os.path.exists(new_file):
                notEmpty = input(f'Файл {new_file} уже существует !! Перезаписать ? у :')
                if notEmpty == 'y':
                    shutil.copy(file_to_copy, new_file)
                    if os.path.exists(new_file):
                        print(f'Файл {new_file} успешно перезаписан!')
                    else:
                        print('Возникли проблемы копирования !!!!!')
                else:
                    print('Файл НЕ перезаписан !')
            else:
                shutil.copy(file_to_copy, new_file)
                if os.path.exists(new_file):
                    print(f'Файл {new_file} успешно создан!')
                else:
                    print("Возникли проблемы копирования !!!!!")

        if task == 'q':
            break
