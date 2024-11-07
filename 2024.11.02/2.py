  
dividoble = int(input("введите делимое: "))
dividor = int(input("введите делитель: "))

if dividoble%dividor:
    print(f""" {dividoble} не делится на {dividor} нацело
 неполное частное: {dividoble//dividor}
 остаток: {dividoble%dividor}""")
else: print(f'''{dividoble} делится на {dividor} нацело
 частное: {dividoble//dividor}
''')

# введите делимое: 10
# введите делитель: 3
 # 10 не делится на 3 нацело
 # неполное частное: 3
 # остаток: 1
 
 # введите делимое: 9
# введите делитель: 3
# 9 делится на 3 нацело
 # частное: 3