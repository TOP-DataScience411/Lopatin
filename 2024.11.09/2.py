
arr = []
str = ''
while True:
    str = input("введите слово: ")
    if str:arr.append(str)
    else: break
if len(arr)==1:
    print(arr[0])
elif len(arr)==0:exit(0)
else:
    for el in arr[:-2]:
        print(el,sep = ", ",end = ", ")
    print(arr[-2],arr[-1],sep = " и ")
    
# введите слово: Помидор
# введите слово: Банан
# введите слово: Пепо
# введите слово: Гесперидиум
# введите слово: Клюква
# введите слово:
# Помидор, Банан, Пепо, Гесперидиум и Клюква