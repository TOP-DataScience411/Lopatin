# ПЕРЕИМЕНОВАТЬ везде: в Python для имён переменных используется змеиный_нижний_регистр или слитныйнижнийрегистр, для имён классов используется ВерблюжийРегистр, для имён условных констант используется ЗМЕИНЫЙ_ВЕРХНИЙ_РЕГИСТР или СЛИТНЫЙВЕРХНИЙРЕГИСТР
CoefficientMileToKilometer = 1.60934
mile = int(input("Введите целое число миль: "))
mileFrac = input("Введите десятичное число миль: ")
mile+=int(mileFrac)/10**len(mileFrac)
# ИСПРАВИТЬ: округлить до одного знака после запятой
# ИСПОЛЬЗОВАТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
print(f"{mile:.2f} миль = {mile*CoefficientMileToKilometer:.2f} км")


# Введите целое число миль: 24901
# Введите десятичное число миль: 4594
# 24901.46 миль = 40074.91 км


# ИТОГ: доработать — 4/5

