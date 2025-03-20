import csv
from pathlib import Path


class CountableNouns:

    db_path = Path('words.csv')
    words = {}

    def __init__(self):
        self.__load_words()


    @classmethod
    def __load_words(cls):
        if not cls.db_path.exists():
            raise FileNotFoundError("Не обнаружена база данных слов")
        with open(cls.db_path,encoding='utf-8') as file:
            reader = csv.reader(file)
            for word,word2,word3 in reader:
                cls.words[word] = tuple([word2,word3])

    @classmethod
    def save_words(cls,word1:str):
        if word1:
            print(f"существительное \"{word1}\" отсутствует в базе")
        else:
            word1= input('введите слово, согласующееся с числительным "один": ')

        word2 = input('введите слово, согласующееся с числительным "два": ')
        word5 = input('введите слово, согласующееся с числительным "пять": ')
        cls.words[word1] = tuple([word2,word5])
        with open(cls.db_path,mode="a",encoding='utf-8') as file:
            writer = csv.writer(file,lineterminator='\n',)
            writer.writerow([word1,word2,word5])

    @classmethod
    def pick(cls,num,word):
        if not word in cls.words.keys():
            cls.save_words(word)


        if num % 10 == 1 and num % 100 != 11:
            return word
        elif 2 <= num % 10 <= 4 and not (12 <= num % 100 <= 14):
            return cls.words[word][0]
        else:
            return cls.words[word][1]

# >>> A=CountableNouns()
# >>> B=CountableNouns()
# >>> A==B
# False
# >>> A.words == B.words
# True
# >>> A.pick(7,"восьмёрка")
# существительное "восьмёрка" отсутствует в базе
# введите слово, согласующееся с числительным "два": восьмёрки
# введите слово, согласующееся с числительным "пять": восьмёрок
# 'восьмёрок'
# >>> quit()
#
# D:\top academy\Data science\Homework\2024.12.15>python -i 4.py
# >>> A=CountableNouns()
# >>> A.pick(7,"восьмёрка")
# 'восьмёрок'
# >>>