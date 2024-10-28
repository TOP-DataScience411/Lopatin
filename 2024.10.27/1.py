
import datetime

year = datetime.datetime.today().year

Name = input("введите имя ")
Surname = input("введите фамилию ")
BirthDate = int(input("введите год рождения "))
print(Surname,Name+',',year-BirthDate)

#   введите имя anna
#   введите фамилию lopato
#   введите год рождения 2011
#   lopato anna, 13