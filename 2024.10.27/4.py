number = int(input(" Введите трёхзначное число: "))
summ = 0
mult = 1
while number:
    summ+= number%10
    mult*= number%10
    number//=10
print(f" Сумма цифр = {summ} Произведение цифр = {mult}")

# Введите трёхзначное число: 496
# Сумма цифр = 19 Произведение цифр = 216