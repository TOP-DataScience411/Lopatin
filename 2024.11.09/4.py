
dic=dict()

while True:
    try:
        key,value = tuple(input("Введите ключ и значение через пробел: ").split())
    except:
        break
    dic[key]=value

value=input("введите значение для поиска ключа: ")

if value in dic.values():
    print(list(dic.keys())[list(dic.values()).index(value)]) # нашёл такой метод поиска по значению на https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary хотел найти способ без использования цикла, хотя под капотом, мне кажется всё равно используются циклы, причём скорее всего менее эффективно
else: print('! value error !')

# Введите ключ и значение через пробел: a 1
# Введите ключ и значение через пробел: b 2
# Введите ключ и значение через пробел: c 3
# Введите ключ и значение через пробел: d 4
# Введите ключ и значение через пробел:
# введите значение для поиска ключа: 2
# b


# Введите ключ и значение через пробел: fd 3
# Введите ключ и значение через пробел: 23
# введите значение для поиска ключа: t
# ! value error !