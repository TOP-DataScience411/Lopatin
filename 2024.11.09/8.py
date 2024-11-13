  
list_of_files = input("введите имена файлов через ';' знак точка с запятой: ").split(';')
list_of_files = list(map(str.strip,list_of_files))
temp = dict()
answ = []
for el in list_of_files:
    if el in temp.keys():
        temp[el] += 1
        answ.append(el.replace('.', f'_{temp[el]}.', 1))
    else:
        temp[el] = 0
        answ.append(el)

answ.sort()

for el in answ:
    print(el)
    
    
# 1.py
# 1_1.py
# 1_2.py
# aux.h
# functions.h
# main.cpp
# main_1.cpp
# main_2.cpp
# src.tar.gz
# src_1.tar.gz