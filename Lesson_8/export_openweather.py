
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

__author__ = 'Шенк Евгений Станиславович'

import csv
import json
import sqlite3
import sys
import os


def db_select(city_name_or_id=None, db_name='Weather_in_cities.db'):
    db = []
    with sqlite3.connect(db_name) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        if city_name_or_id in ['all', 'All', 'ALL', None]:
            cur.execute("select * from weather")
        elif str(city_name_or_id).isnumeric():
            cur.execute(f"select * from weather where id_town = {city_name_or_id}")
        elif not str(city_name_or_id).isnumeric():
            cur.execute(f"select * from weather where town = '{city_name_or_id}'")
        else:
            print('Запрос не верен')
        for row in cur.fetchall():
            id_town, town, date, temperature, id_weather = row
            db.append({'id_town': id_town, 'town':  town, 'date': date,
                       'temperature': temperature, 'id_weather': id_weather})
        return db


def json_file(filename='Weather_DB.json', town=None):
    if os.path.splitext(filename)[1] != '.json':
        filename += '.json'
    if os.path.exists(filename):
        ask = input(f'Файл {filename} уже существует, заменить? y/n ')
        if ask not in ['y', 'да']:
            print('Файл не перезаписан !')
            return ''
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(db_select(town), f)
    if os.path.exists(filename):
        print(f'Файл {filename} успешно создан')
    else:
        print('Файл не создан !')


def csv_file(filename='Weather_DB.csv', town=None):
    if os.path.splitext(filename)[1] != '.csv':
        filename += '.csv'
    if os.path.exists(filename):
        ask = input(f'Файл {filename} уже существует, заменить? y/n ')
        if ask not in ['y', 'да']:
            print('Файл не перезаписан !')
            return ''
    csv.register_dialect('excel-semicolon', delimiter=';')
    with open(filename, 'w', encoding='UTF-8') as csvfile:
        fieldnames = ('id_town', 'town', 'date', 'temperature', 'id_weather')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect='excel-semicolon')
        headers = {name:name for name in fieldnames}
        writer.writerow(headers)
        for i in range(len(db_select(town))):
            data = dict(zip(fieldnames, [str(db_select(town)[i]['id_town']), str(db_select(town)[i]['town']),
                                         str(db_select(town)[i]['date']), str(db_select(town)[i]['temperature']),
                                         str(db_select(town)[i]['id_weather'])]))
            writer.writerow(data)
    if os.path.exists(filename):
        print(f'Файл {filename} успешно создан')
    else:
        print('Файл не создан !')


def html_file(filename='Weather_DB.html', town=None):
    if os.path.splitext(filename)[1] != '.html':
        filename += '.html'
    if os.path.exists(filename):
        ask = input(f'Файл {filename} уже существует, заменить? y/n ')
        if ask not in ['y', 'да']:
            print('Файл не перезаписан !')
            return ''
    with open(filename, 'w', encoding='UTF-8') as f:
        for x in db_select(town):
            f.writelines(str(x))
    if os.path.exists(filename):
        print(f'Файл {filename} успешно создан')
    else:
        print('Файл не создан !')


def print_help(filename=None, town=None):
    print("--help - получение справки")
    print("--csv filename [<город>] - экспорт данных из базы данных погоды в csv файл")
    print("--json filename [<город>] - экспорт данных из базы данных погоды в json файл")
    print("--html filename [<город>] - экспорт данных из базы данных погоды в html файл")


if __name__ == "__main__":
    do = {
        "--help": print_help,
        "--csv": csv_file,
        "--json": json_file,
        "--html": html_file,
        }

    try:
        filename = sys.argv[2]
    except IndexError:
        filename = None

    try:
        town = sys.argv[3]
    except IndexError:
        town = None

    try:
        key = sys.argv[1]
    except IndexError:
        key = None

    if key:
        if do.get(key):
            do[key](filename, town)
        else:
            print("Задан неверный ключ")
            print("Укажите ключ --help для получения справки")
