
__author__ = 'Шенк Евгений Станиславович'

import math
import os

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker:
    def __init__(self, info_line):
        self.info_worker = info_line

    def __get_data_info(self):
        path_data = os.path.join('data', 'hours_of')
        with open(path_data, 'r', encoding='UTF-8') as f:
            data_block = [line.rstrip() for line in f.readlines()]

        return data_block

    def __get_info_to_normal(self):
        table = []
        data = []

        table.append(self.info_worker.split(' '))

        i = 0
        while i < len(self.__get_data_info()):
            data.append(self.__get_data_info()[i].split(' '))
            i += 1

        table = list(filter(len, table[0]))

        i = 0
        while i < len(data):
            data[i] = list(filter(len, data[i]))
            if data[i][0] in table and data[i][1] in table:
                table.append(data[i][2])
            i += 1

        return table

    def get_salary(self):
        salary = []
        tb = self.__get_info_to_normal()
        if tb[5] > tb[4]:
            salary.append([tb[0], tb[1], float(tb[2]) + float(tb[2]) / float(tb[4])
                           * (float(tb[5]) - float(tb[4]))])
        elif tb[5] == tb[4]:
            salary.append([tb[0], tb[1], float(tb[2])])
        else:
            salary.append([tb[0], tb[1], round((float(tb[2]) * float(tb[5])) / float(tb[4]), 2)])

        return salary[0]


if __name__ == "__main__":
    path = os.path.join('data', 'workers')
    with open(path, 'r', encoding='UTF-8') as f:
        info_block = [line.rstrip() for line in f.readlines()]

    print('Зарплаты сотрудников:')
    i = 0
    for line in info_block:
        if 'Имя' not in line:
            try:
                worker = Worker(info_block[i])
                print(f'{worker.get_salary()[0]} {worker.get_salary()[1]}, зарплата - {worker.get_salary()[2]}')
            except ValueError:
                print('Данные в ведомость внесены не верно')
        i += 1
