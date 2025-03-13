from shutil import copy2
from pathlib import Path
import random
from time import perf_counter
import data.vars as CONSTANTS
from importlib.util import spec_from_file_location , module_from_spec

def load_file(path_to_file:Path):
    copy2(path_to_file,Path.cwd() / path_to_file.name)
    return Path.cwd() / path_to_file.name



def inicialization_game():
    path_to_vars = Path().cwd() / 'data' / 'questions.quiz'
    with open(path_to_vars, encoding='utf-8', mode='r') as stream:
        file = stream.read().split('\n\n')

    global all_questions
    all_questions = {}
    for el in file:

        block = el.split('\n')
        all_questions[block[0]] = {}

        for i in block[1:]:
            if i.endswith('+'):
                all_questions[block[0]][i[3:-2]]= True
            else:
                all_questions[block[0]][i[3:]]= False

    path_to_important_function = Path.cwd().parent/ "2024.11.30"/"utils.py"
    spec = spec_from_file_location("my_module", path_to_important_function)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    global message
    message = module.important_message(CONSTANTS.APP_TITLE)


def game():
    print(message,end = "\n\n")
    print(CONSTANTS.HELP,end = "\n\n")
    for el in random.sample(population=sorted(all_questions),k=CONSTANTS.N):
        CONSTANTS.SCORE+=qestion(el)
    print(f"Вы набрали {CONSTANTS.SCORE} очков")



def qestion(question):
    print(question)
    start = perf_counter()

    answers = list(all_questions[question].keys())
    random.shuffle(answers)
    for number,el in enumerate(answers,1):
        print(f'{number}: {el}')

    while True:
        try:
            answer = int(input(CONSTANTS.PROMPT))
            if answer in range(1,5):
                break
        except:
            pass
        print(f"{CONSTANTS.ERR_PREFIX}введите цифру номера ответа{CONSTANTS.ERR_PREFIX[::-1]}")
    end =perf_counter()
    answer = all_questions[question][answers[answer-1]]
    timeleft = end-start
    if not answer:
        print("Неверно...")
        return CONSTANTS.INCORRECT
    if timeleft<CONSTANTS.TIMER :
        print(f"Верно! ({int(timeleft)} с)")
        return CONSTANTS.CORRECT_TIME
    print(f'Верно, но недостаточно быстро. ({int(timeleft)} с)')
    return CONSTANTS.CORRECT_TIMEOUT