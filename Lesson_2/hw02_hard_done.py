
__author__ = 'Шенк Евгений Станиславович'

import math

task = int(input('Введите номер решаемой задачи (1, 2, 3) : '))

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

if task == 1:
    equation = 'y = -12x + 11111140.2121'
    x = float(input(f'Для определения координаты y в уравнении {equation} задайте координату x: '))
    y = 0
    k = ''
    b = ''
    k_0 = 0     # индекс начала коэффициента k
    k_1 = 0     # индекс конца коэффициента k
    equation = equation.replace(' ', '')        # убрали все пробелы в уравнении
    i = 0
    for f in equation:
        if f == '=':        # Коэффициент k - все что между '=' и 'x'
            k_0 = i + 1
        elif f == 'x':
            k_1 = i
        i += 1
    for f in equation[::-1]:        # Коэффициент b - все что между 'x' и концом выражения
        if f == 'x':
            break
        else:
            b = b + str(f)

    k = float(equation[k_0:k_1])
    b = float(b[::-1])
    y = k * x + b

    print(f'y = {y}')

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

if task == 2:
    date = ''
    norm_length = 10
    day = 0
    month = 0
    year = 0
    while True:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        date = input('Введите дату в формате dd.mm.yyyy :')
        try:
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:len(date)])
        except:
            print('Дата введена НЕ в требуемом формате')
            continue
        if (year % 4) == 0:
            days_per_month[1] = days_per_month[1] + 1
        if date[2] != '.' or date[5] != '.':
            print('Дата введена НЕ в требуемом формате')
            continue
        if len(date) != norm_length:
            print('Дата введена НЕ в требуемом формате')
            continue
        if not 1 <= year <= 9999:
            print('Год введён НЕ верно, введите год от 0001 до 9999')
            continue
        if not 1 <= month <= 12:
            print('Месяц введён НЕ верно, введите месяц от 01 до 12')
            continue
        if not 1 <= day <= days_per_month[month - 1]:
            print('День введён НЕ верно, введите месяц от 01 до максимального в нужном месяце')
            continue
        print("Дата введена верно !!!")
        break


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

if task == 3:
    N = ''
    N_floor = 0     # номер этажа
    N_from_the_left = 0     # порядковый номер слева на этаже
    while True:
        N = int(input('Укажите номер комнаты N, 1 ≤ N ≤ 2 000 000 000 : '))
        if 1 <= N <= 2e9:
            break
        else:
            print('Введено значение не входящее в диапазон 1 ≤ N ≤ 2 000 000 000 !!!')

    list_2 = [0]
    i = 1       # i - номер нужного нам блока, а следовательно кол-во столбцов и строк в нем
    while True:
        if list_2[i-1] < N:
            list_2.append(list_2[i-1] + i**2)       # 1**2 + 2**2 + 3**2 + 4**2 + ...
            N_floor += (i - 1)      # Занятые этажи до нужного блока
        else:
            i -= 1
            break
        i += 1

    n_0 = N - list_2[i-1]       # n_0 - номер нужного элемента в блоке, вычетаем из N все эл-ты предыдущих блоков
    N_floor += math.ceil(n_0 / i)       # добавляем этажи занятые в нужном блоке

    if (n_0 % i) == 0:      # Считаем комнату слева
        N_from_the_left = i
    else:
        N_from_the_left = n_0 % i

    print(f'{N_floor} {N_from_the_left}')

