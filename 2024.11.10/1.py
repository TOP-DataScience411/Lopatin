
def strong_password(text=None):
    if !text:return False
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
        