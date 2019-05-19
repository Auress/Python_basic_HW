
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

__author__ = 'Шенк Евгений Станиславович'

import urllib.request
import urllib.parse
import urllib.error
import gzip
import json
import os
import shutil
import sqlite3
import datetime


def download_city_list():
    url_town_list = 'http://bulk.openweathermap.org/sample/city.list.json.gz'
    file_name = url_town_list.split('/')[-1]
    if os.path.exists(file_name):
        ask = input(f'Файл {file_name} уже существует, заменить? y/n ')
        if ask not in ['y', 'да']:
            print('Файл не перезаписан !')
            return ''
    urllib.request.urlretrieve(url_town_list, file_name)


def get_all_countries():
    return sorted(list(set([x["country"] for x in city_dict if x["country"] != ''])))


def get_all_towns_in_country(country_name):
    return [x["name"] for x in city_dict if x["country"] == country_name.upper()]


def get_appid(path='app.id'):
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            return f.readlines()[0][1:]
    except FileNotFoundError:
        print(f'Файл {path} не найден')
        return None


def weather_info(city_id):
    appid = get_appid()
    if appid is not None:
        try:
            url_town_temp = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&appid={appid}'
            response = urllib.request.urlopen(url_town_temp)
            weather_data = json.load(response)
            return {'weather_id': (weather_data["weather"][0]['id']), 'temp': int(weather_data['main']['temp'])}
        except urllib.error.HTTPError:
            print(f'Города с номером {city_id} не существует')
            return None
    else:
        return None


def json_dl(country_names):
    appid = get_appid()
    for i in country_names:
        if i.upper() in get_all_countries():
            if os.path.exists(i.upper()):
                notEmpty = input(f'Папка {i.upper()} уже существует !! Перезаписать ? у :')
                if notEmpty == 'y':
                    shutil.rmtree(i.upper())
                    os.makedirs(i.upper())
                    if os.path.exists(i.upper()):
                        print(f'Папка {i.upper()} успешно перезаписана!')
                    else:
                        print(f'Возникли проблемы при создании папки {i.upper()}!')
                else:
                    print('Папка НЕ перезаписана !')
            else:
                os.makedirs(i.upper())

            city_ids = [x["id"] for x in city_dict if x["country"] == i.upper()]

            for id in city_ids:
                path = os.path.join(os.getcwd(), i.upper(), f'{id}.json')
                try:
                    url_town = f'http://api.openweathermap.org/data/2.5/weather?id={id}&units=metric&appid={appid}'
                    response = urllib.request.urlopen(url_town)
                    town_data = json.load(response)
                    with open(path, 'w', encoding='UTF-8') as f:
                        json.dump(town_data, f)
                except urllib.error.HTTPError:
                    print(f'Города с номером {id} не существует')
                    continue

        else:
            print(f'Обозначения страны {i.upper()} не существует, выведите список доступныз стран')
            continue


def db_create(db_name='Weather_in_cities.db'):
    todo = True if not os.path.exists(db_name) else False
    if os.path.exists(db_name):
        todo = input('Создать новую базу данных? y: ').lower()
    if todo in ['y', 'yes', 'у', 'д', 'да', True]:
        os.remove(db_name)
        with sqlite3.connect(db_name) as conn:
            conn.execute("""
                create table weather (
                    id_town        INTEGER PRIMARY KEY,
                    town           VARCHAR(255),
                    date           DATE,
                    temperature    INTEGER,
                    id_weather     INTEGER
                );
                """)
            print('Новая база данных создана !')
    else:
        print('База данных осталась старая')


def db_fill_web(city_id, db_name='Weather_in_cities.db'):
    if city_id in [x["id"] for x in city_dict]:
        with sqlite3.connect(db_name) as conn:
            for c_d in city_dict:
                if c_d["id"] == city_id:
                    try:
                        conn.execute("""
                            insert into weather (id_town, town, date, temperature, id_weather) VALUES (?,?,?,?,?)""", (
                                c_d["id"],
                                c_d["name"],
                                datetime.date.today(),
                                weather_info(c_d["id"])['temp'],
                                weather_info(c_d["id"])['weather_id']
                            )
                        )
                    except IndexError:
                        pass
                    except TypeError:
                        pass
                    except sqlite3.IntegrityError:
                        conn.execute("update weather set date=:date where id_town=:id_town",
                                     {'id_town': c_d["id"], 'date': datetime.date.today()})
                        conn.execute("update weather set temperature=:temperature where id_town=:id_town",
                                     {'id_town': c_d["id"], 'temperature': weather_info(c_d["id"])['temp']})


def db_select(city_name_or_id=None, db_name='Weather_in_cities.db'):
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
            print("{:7d}".format(id_town),
                  "{:30s}".format(town),
                  "{:11s}".format(date),
                  "{:3d}".format(temperature),
                  "{:4d}".format(id_weather))


def db_from_files(country_names, db_name='Weather_in_cities.db'):
    for c_names in country_names:
        path = os.path.join(os.getcwd(), c_names.upper())
        try:
            cur_files = ([x for x in os.listdir(path) if os.path.splitext(x)[1] == '.json'])

            with sqlite3.connect(db_name) as conn:
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()

                for i in cur_files:
                    file_path = os.path.join(path, i)
                    with open(file_path, 'r') as f:
                        weather_data = json.loads(f.read())
                        for c_d in city_dict:
                            if c_d["id"] == weather_data['id']:
                                try:
                                    conn.execute("""
                                        insert into weather (id_town, town, date, temperature, id_weather) VALUES (?,?,?,?,?)""",
                                                 (
                                                     c_d["id"],
                                                     c_d["name"],
                                                     datetime.date.today(),
                                                     int(weather_data['main']['temp']),
                                                     int(weather_data['weather'][0]['id'])
                                                 )
                                                 )
                                except IndexError:
                                    print('IndexError')
                                    pass
                                except TypeError:
                                    print('TypeError')
                                    pass
                                except sqlite3.IntegrityError:
                                    cur.execute("update weather set date=:date where id_town=:id_town",
                                                {'id_town': weather_data['id'], 'date': datetime.date.today()})
                                    cur.execute("update weather set temperature=:temperature where id_town=:id_town",
                                                {'id_town': weather_data['id'], 'temperature': int(weather_data['main']['temp'])})
        except FileNotFoundError:
            print(f'Системе не удается найти указанный путь: {path}')


if __name__ == "__main__":
    try:
        file_name = 'city.list.json.gz'
        with gzip.open(file_name, 'rb') as f:
            city_dict = json.loads(f.read())
    except FileExistsError:
        download_city_list()

    db_filename = 'Weather_in_cities.db'

while True:
    todo = input('1. Создавать файл базы данных SQLite\n'
                 '2. Вывести список стран\n'
                 '3. Вывести список городов в данной стране\n'
                 '4. Скачать JSON файлы погоды в городах выбранной страны\n'
                 '5. Добавить или обновить базу данных по городам выбранной страны\n'
                 '6. Получить информацию из базы данных\n'
                 '7. Скачать архив с информацией по городам\n'
                 'q. Выход\n').lower()

    if todo == '1':
        db_create()
        continue

    if todo == '2':
        print(f'Список стран: {get_all_countries()}')
        continue

    if todo == '3':
        our_country = input('Укажите кодировку страны (пример: RU) или выход(q): ').upper()
        if our_country not in ['Q', 'Й', '1']:
            print(f'Список городов в стране {our_country}: ')
            for x in get_all_towns_in_country(our_country):
                print(x)
        continue

    if todo == '4':
        our_country = input('Укажите кодировку страны (пример: RU) или выход(q): ').upper()
        if our_country not in ['Q', 'Й', '1']:
            json_dl([our_country])
        continue

    if todo == '5':
        our_country = input('Укажите кодировку страны (пример: RU) или выход(q): ').upper()
        if our_country not in ['Q', 'Й', '1']:
            db_from_files([our_country])
        continue

    if todo == '6':
        req = input('Вывести инфомицию по стране(1) / по городам(2) / всю БД(3) / выход(any key): ')
        if req == '1':
            our_country = input('Укажите кодировку страны (пример: RU) или выход(q): ').upper()
            if our_country not in ['Q', 'Й', '1']:
                for x in get_all_towns_in_country(our_country):
                    db_select(x)
        if req == '2':
            our_city = input('Укажите название или id города (пример: Ordino) или выход(q): ')
            if our_city not in ['q', 'й', 'Q', 'Й', '1']:
                db_select(our_city)
        if req == '3':
            db_select()

    if todo == '7':
        download_city_list()

    if todo in ['q', 'й']:
        break
