num = input("введите номер билета: ")
sum =0
for el in num[:3]:
    sum+=int(el)

for el in num[3:]:
    sum-=int(el)

if not sum:print("да")
else: print("нет")

# введите номер билета: 584526
# нет
# введите номер билета: 456654
# да