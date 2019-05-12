
__author__ = 'Шенк Евгений Станиславович'

import math


class Figure:
    def _get_lengths(self, dot_1, dot_2):
        return math.sqrt(math.pow((dot_2[1] - dot_1[1]), 2) + math.pow((dot_2[0] - dot_1[0]), 2))


class Triangle(Figure):     # Task #1
    def __init__(self, xy_1, xy_2, xy_3):
        try:
            self.x1 = float(xy_1[0])
            self.y1 = float(xy_1[1])
            self.x2 = float(xy_2[0])
            self.y2 = float(xy_2[1])
            self.x3 = float(xy_3[0])
            self.y3 = float(xy_3[1])

            self.xy_1_2 = self._get_lengths(xy_1, xy_2)
            self.xy_2_3 = self._get_lengths(xy_2, xy_3)
            self.xy_3_1 = self._get_lengths(xy_3, xy_1)
        except ValueError:
            print('Значения точек введены не верно, введите численные значения')

    def get_square(self):
        return abs(0.5 * (((self.x2 - self.x1) * (self.y3 - self.y1)) - ((self.x3 - self.x1) * (self.y2 - self.y1))))

    def get_height(self):     # Стороны перпендикулярные высоте
        s = self.get_square()
        try:
            h_1_2 = (s * 2) / self.xy_1_2
        except ZeroDivisionError:
            h_1_2 = None
        try:
            h_2_3 = (s * 2) / self.xy_2_3
        except ZeroDivisionError:
            h_2_3 = None
        try:
            h_3_1 = (s * 2) / self.xy_3_1
        except ZeroDivisionError:
            h_3_1 = None

        return {'AB': h_1_2, 'BC': h_2_3, 'CA': h_3_1}

    def get_perimeter(self):
        return self.xy_1_2 + self.xy_2_3 + self.xy_3_1


class Trapezium(Figure):     # Task #2
    def __init__(self, xy_1, xy_2, xy_3, xy_4):
        try:
            self.xy_1 = xy_1
            self.xy_2 = xy_2
            self.xy_3 = xy_3
            self.xy_4 = xy_4

            self.x1 = float(xy_1[0])
            self.y1 = float(xy_1[1])
            self.x2 = float(xy_2[0])
            self.y2 = float(xy_2[1])
            self.x3 = float(xy_3[0])
            self.y3 = float(xy_3[1])
            self.x4 = float(xy_4[0])
            self.y4 = float(xy_4[1])

            self.xy_1_2 = self._get_lengths(xy_1, xy_2)
            self.xy_2_3 = self._get_lengths(xy_2, xy_3)
            self.xy_3_4 = self._get_lengths(xy_3, xy_4)
            self.xy_4_1 = self._get_lengths(xy_4, xy_1)

            deg = 0  # Угол поворота оси координат
        except ValueError:
            print('Значения точек введены не верно, введите численные значения')

    def __straight(self, dot_1, dot_2):  # Считаем коэф-ты 'a' и 'b' для уравнения y + a * x + b = 0
        if (dot_2[0] - dot_1[0]) != 0:
            a = (dot_1[1] - dot_2[1]) / (dot_2[0] - dot_1[0])  # a = (y1-y2)/(x2-x1)
            b = (dot_1[0] * dot_2[1] - dot_2[0] * dot_1[1]) / (dot_2[0] - dot_1[0])  # b = (x1y2-x2y1)/(x2-x1)
            if a != 0:
                return a, b, ''
            else:
                return 0, 0, 'Error'
        else:
            return 0, 0, 'Error'

    def __rotate(self, dot, alfa):  # Попорачиватель оси координат
        x = dot[0] * math.cos(alfa * math.pi / 180.0) - dot[1] * math.sin(alfa * math.pi / 180.0)
        y = dot[0] * math.sin(alfa * math.pi / 180.0) + dot[1] * math.cos(alfa * math.pi / 180.0)
        return x, y

    def is_a_trapezium(self):
        if self.xy_1 == self.xy_2 or self.xy_1 == self.xy_3 or self.xy_1 == self.xy_4 or self.xy_2 == self.xy_3 or\
                self.xy_2 == self.xy_4 or self.xy_3 == self.xy_4:
            print('некоторые точки совпадают - данные точки не вершины трапеции')
            return False

        if self.__straight(self.xy_1, self.xy_2)[2] == 'Error' or self.__straight(self.xy_3, self.xy_4)[2] == 'Error' \
                or self.__straight(self.xy_2, self.xy_3)[2] == 'Error' or \
                self.__straight(self.xy_1, self.xy_4)[2] == 'Error':  # Проверка на параллельность сторон осям координат
            deg = 30  # Угол поворота оси координат
            self.xy_1 = self.__rotate(self.xy_1, deg)
            self.xy_2 = self.__rotate(self.xy_2, deg)
            self.xy_3 = self.__rotate(self.xy_3, deg)
            self.xy_4 = self.__rotate(self.xy_4, deg)

        if round(self.__straight(self.xy_1, self.xy_2)[1] == round(self.__straight(self.xy_3, self.xy_4)[1])):
            print('Стороны 1-2 и 3-4 лежат друг на друге - данные точки не вершины трапеции')
            return False
        if round(self.__straight(self.xy_2, self.xy_3)[1] == round(self.__straight(self.xy_1, self.xy_4)[1])):
            print('Стороны 2-3 и 1-4 лежат друг на друге - данные точки не вершины трапеции')
            return False

        if self.xy_1_2 == self.xy_3_4 and self.xy_2_3 != self.xy_4_1:
            if round(self.__straight(self.xy_2, self.xy_3)[0], 3) == round(self.__straight(self.xy_4, self.xy_1)[0], 3)\
                    and round(self.__straight(self.xy_1, self.xy_2)[0], 3) != \
                    round(self.__straight(self.xy_3, self.xy_4)[0], 3):
                print('Стороны 1-2 и 3-4 равны, Стороны 2-3 и 1-4 не равны, 2-3 || 1-4, 1-2 не || 3-4')
        elif self.xy_1_2 != self.xy_3_4 and self.xy_2_3 == self.xy_4_1:
            if round(self.__straight(self.xy_2, self.xy_3)[0], 3) != round(self.__straight(self.xy_4, self.xy_1)[0], 3)\
                    and round(self.__straight(self.xy_1, self.xy_2)[0], 3) == \
                    round(self.__straight(self.xy_3, self.xy_4)[0], 3):
                print('Стороны 1-2 не 3-4 равны, Стороны 2-3 и 1-4 равны, 2-3 не || 1-4, 1-2 || 3-4')
        else:
            print('Это не равнобочная трапеция !')
            return False

        print('Это равнобочная трапеция !')
        return True

    def get_length(self):
        return {'Сторона AB': self.xy_1_2, 'Сторона BC': self.xy_2_3, 'Сторона CD': self.xy_3_4,
                'Сторона DA': self.xy_4_1}

    def get_perimeter(self):
        return self.xy_1_2 + self.xy_2_3 + self.xy_3_4 + self.xy_4_1

    def get_square(self):
        a = min(self.xy_1_2, self.xy_2_3, self.xy_3_4, self.xy_4_1)
        b = max(self.xy_1_2, self.xy_2_3, self.xy_3_4, self.xy_4_1)
        c = 0
        for x in (self.xy_1_2, self.xy_2_3, self.xy_3_4, self.xy_4_1):
            if x != a and x != b:
                c = x
        return round(0.5 * (a + b) * math.sqrt(math.pow(c, 2) - math.pow(0.5 * (b - a), 2)), 3)


if __name__ == "__main__":
    while True:
        task = input('Введите номер решаемой задачи (1, 2, q) : ')

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

        if task == '1':
            # tri_1 = Triangle((0, 0), (7, 5), (3, 2))
            while True:
                try:
                    print('Ввод точек сторон треугольника (3 точки):')
                    ax = float(input('Введите координату х точки a :'))
                    ay = float(input('Введите координату y точки a :'))
                    bx = float(input('Введите координату х точки b :'))
                    by = float(input('Введите координату y точки b :'))
                    cx = float(input('Введите координату х точки c :'))
                    cy = float(input('Введите координату y точки c :'))
                except ValueError:
                    print('Значения точек введены не верно, введите численные значения')
                    continue
                else:
                    tri_1 = Triangle((ax, ay), (bx, by), (cx, cy))
                while True:
                    todo = input('Введите чтобы расчитать (1/2/3/4): '
                                 '\n1 - Площадь треугольника \n2 - Высоты треугольника '
                                 '\n3 - Периметр треугольника \n4 - Указать другие координаты\n')
                    if todo == '1':
                        print(f'Площадь треугольника равна {tri_1.get_square()}')
                    if todo == '2':
                        print(f'Высоты треугольника перпендикулярные сторонам равны\n {tri_1.get_height()}')
                    if todo == '3':
                        print(f'Периметр треугольника равен {tri_1.get_perimeter()}')
                    if todo == '4':
                        break
                    else:
                        continue

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

        if task == '2':
            # tra_1 = Trapezium((1, 1), (2, 4), (5, 4), (6, 1))     # ОК
            # tra_1 = Trapezium((1, 0.5), (2, 4), (5, 4), (6, 0.5))     # ОК
            # tra_1 = Trapezium((1, 2), (2, 6), (7, 7), (6, 3))     # not OK
            # tra_1 = Trapezium((2, 3), (4, 5), (6, 7), (8, 9))  # Одна линия
            while True:
                try:
                    print('Ввод точек сторон трапеции (4 точки):')
                    ax = float(input('Введите координату х точки a :'))
                    ay = float(input('Введите координату y точки a :'))
                    bx = float(input('Введите координату х точки b :'))
                    by = float(input('Введите координату y точки b :'))
                    cx = float(input('Введите координату х точки c :'))
                    cy = float(input('Введите координату y точки c :'))
                    dx = float(input('Введите координату х точки d :'))
                    dy = float(input('Введите координату y точки d :'))
                except ValueError:
                    print('Значения точек введены не верно, введите численные значения')
                    continue
                else:
                    tra_1 = Trapezium((ax, ay), (bx, by), (cx, cy), (dx, dy))
                if tra_1.is_a_trapezium():
                    while True:
                        todo = input('Введите чтобы расчитать (1/2/3/4): '
                                     '\n1 - Площадь трапеции \n2 - Длины сторон трапеции '
                                     '\n3 - Периметр трапеции \n4 - Указать другие координаты\n')
                        if todo == '1':
                            print(f'Площадь трапеции равна {tra_1.get_square()}')
                        if todo == '2':
                            print(f'Длины сторон трапеции равны\n {tra_1.get_length()}')
                        if todo == '3':
                            print(f'Периметр трапеции равен {tra_1.get_perimeter()}')
                        if todo == '4':
                            break
                        else:
                            continue
                else:
                    continue

        if task == 'q':
            break
