
scores_letters = {
    1: 'АВЕЁИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = input("введите слово: ")
word = word.upper()
score = 0
for el in word:
    for key,value in scores_letters.items():
        if el in value:
            score+=key
            break



print(f"слово {word} набрало {score} очков")



# введите слово: шаурма
# слово ШАУРМА набрало 15 очков

# введите слово: флюгегехаймен
# слово ФЛЮГЕГЕХАЙМЕН набрало 40 очков

