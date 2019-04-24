
__author__ = 'Шенк Евгений Станиславович'

while True:
    task = int(input('Введите номер решаемой задачи (1, 2, 3, 4, 0) : '))

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

    if task == 1:
        def fibonacci(n, m):
            if n > m:
                return 'Аргумент 1 больше аргумента 2 !!!'
            fibo = [1, 1]
            i = 2
            while i <= m:
                fibo.append(fibo[i-2]+fibo[i-1])
                i += 1
            return fibo[n:m+1]      # Возвращает все элементы с n-элемента до m-элемента !включительно!


        a = int(input('Введите индекс начального элемента ряда Фибоначчи - '))
        b = int(input('Введите индекс конечного (включительно) элемента ряда Фибоначчи - '))
        print(fibonacci(a, b))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

    if task == 2:
        def sort_to_max(origin_list):
            j = 0
            while j < len(origin_list):
                i = j
                while i < len(origin_list):
                    if origin_list[j] > origin_list[i]:
                        origin_list[j], origin_list[i] = origin_list[i], origin_list[j]
                    i += 1
                j += 1
            return origin_list

        print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

    if task == 3:
        def my_filter(func, iter):
            new_list = []
            i = 0
            for f in iter:
                if func(f):
                    new_list.append(f)
                i += 1
            return new_list


        a = [3, 4, 5, 6, 7, 8]
        b = [45, 9, 'gogo', '55', '']
        My_filter_test_1 = (list(my_filter(lambda x: x > 5, a)))
        My_filter_test_2 = (list(my_filter(lambda x: str(x).isnumeric(), b)))
        print(My_filter_test_1)
        print(My_filter_test_2)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

    if task == 4:
        import math

        def straight(dot_1, dot_2):        # Считаем коэф-ты 'a' и 'b' для уравнения y + a * x + b = 0
            a = (dot_1[1] - dot_2[1]) / (dot_2[0] - dot_1[0])       # a = (y1-y2)/(x2-x1)
            b = (dot_1[0] * dot_2[1] - dot_2[0] * dot_1[1]) / (dot_2[0] - dot_1[0])     # b = (x1y2-x2y1)/(x2-x1)
            return a, b


        def line(dot_1, dot_2):     # Считаем длину линии от точки 1 до точки 2
            length = math.sqrt(math.pow(math.fabs(dot_2[0] - dot_1[0]), 2) +
                               math.pow(math.fabs(dot_2[1] - dot_1[1]), 2))
            return length

        A_1 = (1, 2)
        A_2 = (2, 6)
        A_3 = (7, 7)
        A_4 = (6, 3)

        if round(line(A_2, A_1), 3) == round(line(A_3, A_4), 3):
            print('Стороны А_1А_2 и А_3А_4 равны')
            if round(line(A_2, A_3), 3) == round(line(A_1, A_4), 3):
                print('Стороны А_2А_3 и А_1А_4 равны')
                # 1)Линии параллельны, коэф-ты 'а' равны 2)Линии не лежат, друг на друге, коэф-ты 'b' не равны
                if round(straight(A_2, A_3)[0], 3) == round(straight(A_1, A_4)[0], 3):
                    if straight(A_2, A_3)[1] != straight(A_1, A_4)[1]:
                        print('Стороны А_2А_3 и А_1А_4 параллельны')
                        print('Это параллелограмм !')
                    else:
                        print('Стороны А_2А_3 и А_1А_4 лежат друг на друге - данные точки не вершины параллелограмма')
                else:
                    print('Стороны А_2А_3 и А_1А_4 не параллельны - данные точки не вершины параллелограмма')
            else:
                print('Стороны А_2А_3 и А_1А_4 не равны - данные точки не вершины параллелограмма')
        else:
            print('Стороны А_1А_2 и А_3А_4 не равны - данные точки не вершины параллелограмма')

    if task == 0:
        break
