
__author__ = 'Шенк Евгений Станиславович'

import os

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Pupil:
    def __init__(self, pupils, fio):
        self.pupils = pupils
        self.fio = fio

    def info_parents(self):
        father = [elem.split(';')[1] for elem in self.pupils if elem.split(';')[0] == self.fio]
        mother = [elem.split(';')[2] for elem in self.pupils if elem.split(';')[0] == self.fio]
        return father, mother


class School:
    def __init__(self, pupils, teachers):
        self.pupils = pupils
        self.teachers = teachers

    def get_classes(self):
        class_nums = [elem.split(';')[3] for elem in self.pupils]
        return sorted(set(class_nums))

    def get_teachers(self, class_num):
        teachers_list = [elem.split(';')[0] for elem in self.teachers if class_num in elem]
        sbj_list = [elem.split(';')[1] for elem in self.teachers if class_num in elem]
        return list(map(list, zip(teachers_list, sbj_list)))

    def get_subjects(self, fio):
        st_name = fio
        st_class = [elem.split(';')[3] for elem in self.pupils if elem.split(';')[0] == st_name][0]
        teacher = [elem.split(';')[0] for elem in self.teachers if st_class in elem]
        sbj = [elem.split(';')[1] for elem in self.teachers if st_class in elem]
        return st_name, st_class, list(map(list, zip(teacher, sbj)))

    def get_pupils(self, class_num):
        pupils_list = [elem.split(';')[0] for elem in self.pupils if elem.split(';')[3] == class_num]
        return pupils_list

    def get_all_pupils(self):
        pupils_list = [elem.split(';')[0] for elem in self.pupils]
        return pupils_list


path = os.path.join('data', 'pupils.txt')
with open(path, 'r', encoding='UTF-8') as f:
    pupils_block = [line.rstrip() for line in f.readlines() if line.rstrip() != '\ufeff']

path = os.path.join('data', 'teachers.txt')
with open(path, 'r', encoding='UTF-8') as f:
    teachers_block = [line.rstrip() for line in f.readlines() if line.rstrip() != '\ufeff']

if __name__ == "__main__":
    new_school = School(pupils_block, teachers_block)
    print('Добро пожаловать в школу')
    while True:
        todo = input('Введите чтобы получить (1/2/3/4/5/q): \n1 - Полный список всех классов школы '
                     '\n2 - Список всех учеников в указанном классе \n3 - Список всех предметов указанного ученика '
                     '\n4 - ФИО родителей указанного ученика \n5 - Список всех Учителей, преподающих в указанном классе'
                     '\nq - Выход\n')

        if todo == '1':
            print('Полный список всех классов школы: ' + ', '.join(new_school.get_classes()))
            continue

        if todo == '2':
            our_class = input('Укажите класс: ').lower()        # 7б
            if our_class in new_school.get_classes():
                print(f'Ученики {our_class} класса:')
                print('\n'.join(sorted(new_school.get_pupils(our_class))))
            else:
                print('Класс указан не верно, ознакомтесь со списком классов (1)')

        if todo == '3':
            our_pupil = input('Укажите полные ФИО ученика: ')       # Афанасьев Адам Евсеевич
            if our_pupil in new_school.get_all_pupils():
                print(f'{new_school.get_subjects(our_pupil)[0]} ученик {new_school.get_subjects(our_pupil)[1]} класса')
                print('Учителя:')
                for x in new_school.get_subjects(our_pupil)[2:][0]:
                    print(f'{x[0]} - предмет: {x[1]}')
            else:
                print('ФИО ученика указано не верно, ознакомтесь со списком учеников в классе (2)')

        if todo == '4':
            our_pupil = input('Укажите полные ФИО ученика: ')  # Афанасьев Адам Евсеевич
            if our_pupil in new_school.get_all_pupils():
                new_pupil = Pupil(pupils_block, our_pupil)
                print('ФИО родителей указанного ученика: ')
                print(f'Отец ученика - {new_pupil.info_parents()[0][0]}\n'
                      f'Мать ученика - {new_pupil.info_parents()[1][0]}')
            else:
                print('ФИО ученика указано не верно, ознакомтесь со списком учеников в классе (2)')

        if todo == '5':
            our_class = input('Укажите класс: ').lower()        # 7б
            if our_class in new_school.get_classes():
                print(f'Учителя {our_class} класса:')
                for x in new_school.get_teachers(our_class):
                    print(f'{x[0]} - предмет: {x[1]}')
            else:
                print('Класс указан не верно, ознакомтесь со списком классов (1)')

        if todo == 'q':
            break
