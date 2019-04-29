
__author__ = 'Шенк Евгений Станиславович'

import re
import random
import os

while True:
    task = input('Введите номер решаемой задачи (1, 2, 3, q) : ')


# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

    if task == '1':
        line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
               'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
               'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
               'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
               'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
               'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
               'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
               'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
               'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
               'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
               'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
               'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
               'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
               'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
               'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

        res = re.findall(r'[a-z]+', line)
        print(res)

        line_without_re = []
        lowercase_eng_letters = list(map(chr, range(ord('a'), ord('z') + 1)))
        block = ''
        for f in line:
            if f in lowercase_eng_letters:
                block += f
            else:
                line_without_re.append(block)
                block = ''
        line_without_re.append(block)
        line_without_re = list(filter(len, line_without_re))
        print(line_without_re)



           # Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

    if task == '2':
        line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
              'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
              'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
              'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
              'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
              'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
              'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
              'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
              'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
              'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
              'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
              'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
              'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
              'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
              'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

        res = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2)
        print(res)

        line_without_re = []
        lowercase_eng_letters = list(map(chr, range(ord('a'), ord('z') + 1)))
        uppercase_eng_letters = list(map(chr, range(ord('A'), ord('Z') + 1)))
        block = ''
        for f in line_2:
            if f in lowercase_eng_letters:
                if len(block) <= 1:
                    block += f
                if len(block) == 2:
                    block = block[1] + f
                if 2 < len(block) < 5:
                    block = ''
                    block += f
                if len(block) >= 5:
                    line_without_re.append(block[2:-2])
                    block = ''
                    block += f
            else:
                if len(block) <= 1:
                    block = ''
                else:
                    block += f
        if len(block) >= 5:
            line_without_re.append(block[2:-2])

        print(line_without_re)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

    if task == '3':
        path = os.path.join('data', 'LargeNumber.txt')
        my_file = open(path, 'w', encoding='UTF-8')
        i = 0
        while i < 2500:
            my_file.write(str(random.randint(0, 9)))
            i += 1
        my_file.close()

        path = os.path.join('data', 'LargeNumber.txt')
        with open(path, 'r', encoding='UTF-8') as my_file:
            number = my_file.readline()
        i = 0
        max_sequence = ''
        same_length = []
        block = '0'
        blocks = []
        for f in number:           # Ищем самую длинную последовательность
            if f == block[0]:
                block += f
            else:
                if len(block) > len(max_sequence):
                    max_sequence = block
                block = f
        if len(block) > len(max_sequence):
            max_sequence = block

        for f in number:           # Ищем другие последовательности такой же длины
            if f == block[0]:
                block += f
            else:
                if len(block) == len(max_sequence):
                    same_length.append(block)
                block = f
        if len(block) == len(max_sequence):
            same_length.append(block)

        print(f'Самые длинные последовательности : {same_length}')

    if task == 'q':
        break
