import shutil
from textwrap import wrap


def important_message(text:str):
    width = shutil.get_terminal_size().columns - 1
    text_list = wrap(text,width-2)
    formated_text_list = formating_text(text_list,width)


    improved_text = "#"+"="*(width-2)+"#"+'\n'+"#"+" "*(width-2)+"#"+'\n'

    for el in formated_text_list:
        improved_text+=el

    improved_text += "#" + " " * (width - 2) + "#" + '\n' + "#" + "=" * (width - 2) + "#"

    return improved_text


def formating_text(text,width):
    formated_text = []
    for el in text:
        formated_text.append("# " + el.center(width - 4, " ") + " #" + "\n")
    return formated_text