
mail = input("введите email: ")
dog = mail.find("@")
dot = mail.find(".",dog+1)
if dog!=-1 and dot != -1 :
    print("да")
else: print("нет")

# введите email: po.mail@com
# нет

# введите email: lopavel@gmail.com
# да