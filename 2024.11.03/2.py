
try:
    lengh = int(input("введите длину списка: "))
    if lengh<0:
        raise ValueError
except ValueError as ValEr:
    print("необходимо ввести целое положительное число")

arr = []

while lengh:
    lengh-=1
    arr.append(int(input("введите число: ")))

sum=0
for el in arr:
    if el>0:
        sum+=el

print(f"сумма всех положительных чисел = {sum}")

# введите длину списка: 10
# введите число: 7
# введите число: 5
# введите число: 3
# введите число: -100000
# введите число: 5
# введите число: 6
# введите число: 3
# введите число: 6
# введите число: 7
# введите число: 9
# сумма всех положительных чисел = 51