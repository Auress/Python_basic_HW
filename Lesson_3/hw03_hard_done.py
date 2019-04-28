
__author__ = 'Шенк Евгений Станиславович'

import math
import os

while True:
    task = int(input('Введите номер решаемой задачи (1, 2, 3, 0) : '))

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

    if task == 1:
        # enter = '5/6 + 4/7'
        enter = '-2/3 - -2'
        # enter = '5/10 - 4/10'
        # enter = '-2/3 - 2 1/3'
        print(f'Решение {enter} :')
        slicer = enter.split(' ')
        integer = [0, 0, 0]
        numerator = [0, 0, 0]
        denominator = [0, 0, 0]
        sign = ''
        j = 0

        for f in slicer:
            if '/' in f:
                numerator[j] = int(f.split('/')[0])
                denominator[j] = int(f.split('/')[1])
            elif f == '-' or f == '+':
                sign = f
                j = 1
            else:
                integer[j] = int(f)

        if denominator[0] == 0:
            denominator[0] = denominator[1]
        if denominator[1] == 0:
            denominator[1] = denominator[0]
        if denominator[0] == 0 and denominator[1] == 0:
            denominator[0] = 1
            denominator[1] = 1

        i = 0
        while i < 2:
            if integer[i] < 0:
                numerator[i] = numerator[i] * -1
            i += 1

        i = 0
        while i < 2:
            numerator[i] += integer[i] * denominator[i]
            i += 1

        if sign == '-':
            numerator[1] = numerator[1] * -1

        numerator[2] = numerator[0] * denominator[1] + numerator[1] * denominator[0]

        denominator[2] = denominator[0] * denominator[1]

        if numerator[2] > 0:
            while numerator[2] >= denominator[2]:
                numerator[2] -= denominator[2]
                integer[2] += 1
        else:
            while math.fabs(numerator[2]) >= denominator[2]:
                numerator[2] = int(math.fabs(numerator[2]) - denominator[2])
                integer[2] -= 1

        i = 2
        while i <= numerator[2]:
            if numerator[2] % i == 0 and denominator[2] % i == 0:
                numerator[2] = int(numerator[2] / i)
                denominator[2] = int(denominator[2] / i)
            i += 1

        if numerator[2] == 0:
            answer = f'{integer[2]}'
        elif integer[2] != 0:
            answer = f'{integer[2]} {numerator[2]}/{denominator[2]}'
        else:
            answer = f'{numerator[2]}/{denominator[2]}'

        print(answer)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

    if task == 2:
        path = os.path.join('data', 'workers')
        f = open(path, 'r', encoding='UTF-8')
        info_block = [line.rstrip() for line in f.readlines()]
        path = os.path.join('data', 'hours_of')
        f = open(path, 'r', encoding='UTF-8')
        data_block = [line.rstrip() for line in f.readlines()]
        table = []
        data = []
        salary = []
        i = 1
        while i < len(info_block):
            table.append(info_block[i].split(' '))
            i += 1

        i = 1
        while i < len(data_block):
            data.append(data_block[i].split(' '))
            i += 1

        i = 0
        while i < len(table):
            table[i] = list(filter(len, table[i]))
            i += 1

        i = 0
        while i < len(table):
            data[i] = list(filter(len, data[i]))
            i += 1

        for tb in table:
            for dt in data:
                if dt[0] == tb[0] and dt[1] == tb[1]:
                    if dt[2] > tb[4]:
                        salary.append([dt[0], dt[1], float(tb[2]) + float(tb[2]) / float(tb[4])
                                       * (float(dt[2]) - float(tb[4]))])
                    elif dt[2] == tb[4]:
                        salary.append([dt[0], dt[1], float(tb[2])])
                    else:
                        salary.append([dt[0], dt[1], round((float(tb[2]) * float(dt[2])) / float(tb[4]), 2)])

        print("Зарплаты сотрудников")
        print('\n'.join(map(str, salary)))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

    if task == 3:
        path = os.path.join('data', 'fruits.txt')
        f = open(path, 'r', encoding='UTF-8')
        fruit_block = [line.rstrip() for line in f.readlines()]

        fruit_block = list(filter(len, fruit_block))

        for letter in (list(map(chr, range(ord('А'), ord('Я')+1)))):
            i = 0
            for fruit in fruit_block:
                if fruit[0] == letter and i == 0:       # Нужно создать папку data\FruitList
                    path = os.path.join('data', 'FruitList', f'fruits_{letter}.txt')
                    my_file = open(path, 'w', encoding='UTF-8')
                    my_file.write(fruit + '\n')
                    my_file.close()
                    i += 1
                elif fruit[0] == letter and i != 0:
                    path = os.path.join('data', 'FruitList', f'fruits_{letter}.txt')
                    my_file = open(path, 'a', encoding='UTF-8')
                    my_file.write(fruit + '\n')
                    my_file.close()
                else:
                    pass
        print('Папка FruitList наполнена !')

    if task == 0:
        break
