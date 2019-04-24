
__author__ = 'Шенк Евгений Станиславович'

task = int(input('Введите номер решаемой задачи (1, 2, 3) : '))

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

if task == 1:
    fruits = ["яблоко", "банан", "киви", "арбуз"]
    max_len = 0

    for ln in fruits:
        if max_len < len(ln):
            max_len = len(ln)

    i = 1
    for f in fruits:
        print('{0}.{1}{2}'.format(i,' '*(max_len-len(f)), f))
        i += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

if task == 2:
    list_1 = [1, 2, 3, 'три', 5, 6, 7, 8, 9, 10, "два", 3, "банан", "раз", "арбуз"]
    list_2 = [9, 6, 3, 'три', 'шесть', 'девять']

    for f_1 in list_2:
        i = 0
        for f_2 in list_1:
            if f_2 == f_1:
                del list_1[i]
            i += 1

    print(list_1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

if task == 3:
    list_of_num = [6, 7, 8, 9, 23, 34, 45, 56, 78, 89, 95, 65, 64, 63, 62, 61]
    i = 0
    for f in list_of_num:
        if (f % 2) == 0:
            list_of_num[i] = list_of_num[i] / 4
        else:
            list_of_num[i] = list_of_num[i] * 2
        i += 1
    print(list_of_num)