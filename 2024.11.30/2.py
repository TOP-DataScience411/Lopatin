from utils import important_message
import random

def main():
    message = input("введите сообщение: ")
    prepared_message = important_message(message)
    print(prepared_message)
    

main()

