
arr1 =list(map(int,input("Введите первый список: ").split()))
arr2 = list(map(int,input("Введите второй список: ").split()))

i=0
j=len(arr2)

while True:
    if arr1[i:j]==arr2:
        print("да")
        exit()
    i+=1
    j+=1
    if j>len(arr1)+1:
        break

print("нет")

# Введите первый список: 1 2 3 4 5 6 7 8 9  11 25
# Введите второй список: 11 25
# да