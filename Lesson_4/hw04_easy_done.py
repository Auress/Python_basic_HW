
__author__ = 'Шенк Евгений Станиславович'

import random
import os

while True:
    task = input('Введите номер решаемой задачи (1, 2, 3, q) : ')

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

    if task == '1':
        list_random_elem = [random.randint(-100, 100) for elem in range(random.randint(0, 40))]
        list_square_elem = [(elem**2) for elem in list_random_elem]
        print(f'   Список случайных чисел: {list_random_elem}')
        print(f'Квадраты элементов списка: {list_square_elem}')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

    if task == '2':
        path = os.path.join('data', 'fruits.txt')       # Фрукты взяты из прошлого Д/З
        f = open(path, 'r', encoding='UTF-8')

        fruit_block = list(filter(len, [line.rstrip() for line in f.readlines()]))

        fruit_random_list_1 = sorted([random.choice(fruit_block) for elem in range(random.randint(0, len(fruit_block)))])
        fruit_random_list_2 = sorted([random.choice(fruit_block) for elem in range(random.randint(0, len(fruit_block)))])

        fruit_coincidence = [elem for elem in fruit_random_list_1 if elem in fruit_random_list_2]

        print(f'Первый список фруктов: {fruit_random_list_1}')
        print(f'Второй список фруктов: {fruit_random_list_2}')
        print(f'           Совпадения: {fruit_coincidence}')

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

    if task == '3':
        list_random_elem = [random.randint(-1000, 1000) for elem in range(random.randint(10, 100))]
        new_list = [elem for elem in list_random_elem if (elem % 3) == 0 and elem > 0 and (elem % 4) != 0]
        print(f'               Список случайных чисел: {list_random_elem}')
        print(f'Список чисел соответствующий условиям: {new_list}')

    if task == 'q':
        break
