import datetime
import random
from pathlib import Path
from datetime import date,timedelta


def load_data():
    global name
    name = dict()
    path_to_data = Path.cwd() / "data" / "names"
    with open(path_to_data / 'женские_имена.txt',encoding="utf-8",mode="r") as ref:
        name["ЖИ"]=ref.readlines()

    with open(path_to_data / 'мужские_имена_отчества.txt',encoding="utf-8",mode="r") as ref:
        name["МИ"] = []
        name["ЖО"] = []
        name["МО"] = []
        while True:
            content = ref.readline()
            if not content:break
            stroka = [el.replace(',',"").replace('(','').replace(')','') for el in content.split()]
            name["МИ"].append(stroka[0])
            name["МО"].append(stroka[1])
            name["ЖО"].append(stroka[2])

    with open(path_to_data / 'фамилии.txt', encoding="utf-8", mode="r") as ref:
        name["МФ"] = []
        name["ЖФ"] = []
        while True:
            content = ref.readline().split()
            if not content:break
            name["МФ"].append(content[0][:-1])
            name["ЖФ"].append(content[-1])










def generate_person():
    global name

    if bool(random.getrandbits(1)):
        gender = "женский"
        name_of_person = random.choice(name["ЖИ"])
        surname = random.choice(name["ЖФ"])
        patr = random.choice(name["ЖО"])
    else:
        gender = "мужской"
        name_of_person = random.choice(name["МИ"])
        surname = random.choice(name["МФ"])
        patr = random.choice(name["МО"])

    person = {}
    person['имя']= name_of_person
    person['отчество'] = patr
    person['фамилия'] = surname
    person['пол'] = gender
    person['дата рождения'] = date.today() - timedelta(days=365*100)
    person['мобильный'] = f"+79{random.randint(100000000,999999999)}"
    return person

#
# >>> generate_person()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "D:\top academy\Data science\Homework\2024.12.14\2.py", line 54, in generate_person
#     name_of_person = random.choice(name["МИ"])
#                                    ^^^^
# NameError: name 'name' is not defined
# >>> load_data()
# >>> generate_person()
# {'имя': 'Касима\n', 'отчество': 'Пантелеевна', 'фамилия': 'Василевская', 'пол': 'женский', 'дата рождения': datetime.date(1925, 4, 4), 'мобильный': '+79998297600'}
# >>> generate_person()
# {'имя': 'Самуил', 'отчество': 'Олегович', 'фамилия': 'Несветаев', 'пол': 'мужской', 'дата рождения': datetime.date(1925, 4, 4), 'мобильный': '+79173420909'}
# >>> generate_person()
# {'имя': 'Хрисанф', 'отчество': 'Епифанович', 'фамилия': 'Боровский', 'пол': 'мужской', 'дата рождения': datetime.date(1925, 4, 4), 'мобильный': '+79432381787'}
# >>> generate_person()
# {'имя': 'Евдоким', 'отчество': 'Аггеевич', 'фамилия': 'Сотников', 'пол': 'мужской', 'дата рождения': datetime.date(1925, 4, 4), 'мобильный': '+79287797406'}
# >>> generate_person()
# {'имя': 'Зульфия\n', 'отчество': 'Анисиевна', 'фамилия': 'Кондратьева', 'пол': 'женский', 'дата рождения': datetime.date(1925, 4, 4), 'мобильный': '+79126153973'}


