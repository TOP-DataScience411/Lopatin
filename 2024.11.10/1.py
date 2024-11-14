  # ==========  1  ==========  

# Написать функцию с именем strong_password, которая проверяет, является ли пароль надёжным.

# Функция принимает обязательным позиционно-ключевым аргументом пароль в виде объекта str.

# Функция возвращает объект bool.

# Пароль считается надёжным, если соблюдены все нижеследующие условия:
    # - длина пароля составляет восемь символов и более
    # - в пароле присутствуют буквенные символы в обоих регистрах
    # - в пароле присутствуют минимум два символа цифр
    # - кроме символов букв и цифр в пароле присутствуют символы прочих категорий (пробел, знаки пунктуации, диакритические знаки и т.п.)

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
    # >>> strong_password('aP3:kD_l3')
    # True
    # >>> strong_password('password')
    # False
    
def strong_password(text:str):
    flag1 = False
    flag2 = False
    flag3 = False
    digitCount=0
    if len(text) < 8:
        return False
    for el in text:
        if el.isupper():flag1=True
        if el.islower():flag2 =True
        if el.isspace():flag3=True
        if el.isdigit():digitCount+=1
    return flag1 and flag2 and flag3 and digitCount>1
    
    # D:\top academy\Data science\Homework\2024.11.10>python -i 1.py
# >>> print(strong_password(")~qiyH w7d4"))
# True
        