from utils import important_message
import random

def main():
    message = input("введите сообщение: ")
    prepared_message = important_message(message)
    print(prepared_message)
    

main()

#D:\top academy\Data science\Homework\2024.11.30>python -i 2.py
#введите сообщение: This is very very important important message message
#=================================================#
#                                                 #
#  This is very very important important message  #
#                     message                     #
#                                                 #
#=================================================#
#>>> print(important_message("в этом сообщении я расширил командную строку, чтобы проверить расширится лирамка отформатированного сообщения"))
#================================================================================================================#
#                                                                                                                #
# в этом сообщении я расширил командную строку, чтобы проверить расширится лирамка отформатированного сообщения  #
#                                                                                                                #
#================================================================================================================#
