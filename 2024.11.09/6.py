
avalible = {'0','1'}

number = input("введите двоичное число: ")
start =0

if number[0] == 'b':
    start=1
if number[:1] == '0b':
    start = 2
    
for el in number[start:]:
    if el not in avalible:
        print("нет")
        exit()
        
print("да")
        
# введите двоичное число: 010012001
# нет

# введите двоичное число: b01110001
# да