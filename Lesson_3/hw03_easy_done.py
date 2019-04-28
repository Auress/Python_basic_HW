
__author__ = 'Шенк Евгений Станиславович'

while True:
    task = int(input('Введите номер решаемой задачи (1, 2, 3, 0) : '))

    # Задание-1:
    # Напишите функцию, округляющую полученное произвольное десятичное число
    # до кол-ва знаков (кол-во знаков передается вторым аргументом).
    # Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
    # Для решения задачи не используйте встроенные функции и функции из модуля math.

    if task == 1:
        def my_round(number, ndigits):
            if not type(number) == float:
                return 'Аргумент 1 не float !!!'
            if not type(ndigits) == int:
                return 'Аргумент 2 не int !!!'
            integer_part = number // 1
            fractional_part = ((number % 1) * (10 ** (ndigits + 1))) // 1
            if (fractional_part % 10) >= 5:
                fractional_part += 10 - (fractional_part % 10)
            else:
                fractional_part += 0 - (fractional_part % 10)
            fractional_part = fractional_part / (10 ** (ndigits+1))
            return integer_part + fractional_part


        print(my_round(2.1234567, 5))
        print(my_round(2.1999967, 5))
        print(my_round(2.9999967, 5))
        print(my_round('test', 5))

    # Задание-2:
    # Дан шестизначный номер билета. Определить, является ли билет счастливым.
    # Решение реализовать в виде функции.
    # Билет считается счастливым, если сумма его первых и последних цифр равны.
    # !!!P.S.: функция не должна НИЧЕГО print'ить

    if task == 2:
        def lucky_ticket(ticket_number):
            if not type(ticket_number) == int:
                return 'Аргумент не int !!!'
            left_side = 0
            right_side = 0
            left_sum = 0
            right_sum = 0
            t_len = len(str(ticket_number))
            if (t_len % 2) == 0:
                left_side = int(ticket_number // 10**(t_len / 2))
                right_side = int(ticket_number % 10**(t_len / 2))
            else:
                left_side = int(ticket_number // 10**(int(t_len / 2) + 1))
                right_side = int(ticket_number % 10**(int(t_len / 2)))
            for i in str(left_side):
                left_sum += int(i)
            for i in str(right_side):
                right_sum += int(i)
            if left_sum == right_sum:
                return 'Счастливый билет !'
            else:
                return 'Попробуйте еще раз !'

        print(lucky_ticket(123006))
        print(lucky_ticket(12321))
        print(lucky_ticket(436751))
        print(lucky_ticket(123456))
        print(lucky_ticket('kj'))

    if task == 0:
        break
