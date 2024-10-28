# ВВОД/ВЫВОД, ПЕРЕМЕННЫЕ, ТИПЫ ДАННЫХ

  # ==========  1  ==========

# Написать программу для сбора данных о пользователе.

# В первой строке попросить пользователя ввести имя.
# Во второй строке попросить пользователя ввести фамилию.
# В третьей строке попросить пользователя ввести год рождения.

# Программа должна вывести сначала фамилию, потом имя, затем возраст пользователя. 
# Возраст — число лет — считать без учёта дня и месяца рождения.
# Соблюсти формат вывода, показанный в примере ниже.

# Для вывода использовать один вызов функции print. 
# В этой задаче НЕ использовать f-строки.

# Пример ввода:
    # Введите имя: Иван
    # Введите фамилию: Петров
    # Введите год рождения: 2009

# Пример вывода:
    # Петров Иван, 12

import datetime

year = datetime.datetime.today().year

print(year)

Name = input("введите имя ")
Surname = input("введите фамилию ")
BirthDate = int(input("введите год рождения "))
print(Surname,Name+',',year-BirthDate)
