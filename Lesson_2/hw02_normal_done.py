
__author__ = 'Шенк Евгений Станиславович'

import math
import random

task = int(input('Введите номер решаемой задачи (1, 2, 3, 4) : '))

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

if task == 1:
    num_list = [2, -5, 8, 9, -25, 25, 4]
    new_num_list =[]
    for f in num_list:
        if f < 0:
            pass
        elif math.sqrt(f) == int(math.sqrt(f)):
            new_num_list.append(int(math.sqrt(f)))
        else:
            pass

    print(new_num_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

if task == 2:
    days_list = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое',
                 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шеснадцатое',
                 'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе',
                 'двадцать третье', 'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое',
                 'двадцать восьмое', 'двадцать девятое', 'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                  'ноября', 'декабря']
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date = input('Введите дату в формате dd.mm.yyyy :')
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])
    if (year % 4) == 0:
        days_per_month[1] = days_per_month[1] + 1
    if 1 <= month <= 12:
        if 1 <= day <= days_per_month[month - 1]:
            print(f'{days_list[day - 1]} {month_list[month - 1]} {year} года')
        else:
            print('День введён НЕ верно !!!')
    else:
        print('Месяц введён НЕ верно !!!')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

if task == 3:
    rnd_list = []
    n = int(input('Введите количество случайных элементов в списке: '))
    i = 0
    while i < n:
        rnd_list.append(random.randint(-100, 100))
        i += 1
    print(rnd_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

if task == 4:
    list_random_int = [1, 2, 4, 5, 6, 2, 5, 2]
    list_1 = list(set(list_random_int))
    list_2 = []
    list_doubles = []
    i = 0
    for f in list_random_int:
        list_random_int[i] = []
        if f in list_doubles:
            pass
        elif f in list_random_int:
            list_doubles.append(f)
        else:
            list_2.append(f)
        i += 1

    print(f'неповторяющиеся элементы исходного списка: {list_1}')
    print(f'элементы исходного списка, которые не имеют повторений: {list_2}')
