CoefficientMileToKilometer = 1.60934
mile = int(input("Введите целое число миль: "))
mileFrac = input("Введите десятичное число миль: ")
mile+=int(mileFrac)/10**len(mileFrac)
print(f"{mile:.2f} миль = {(mile*CoefficientMileToKilometer):.2f} км")

# Введите целое число миль: 24901
# Введите десятичное число миль: 4594
# 24901.46 миль = 40074.91 км