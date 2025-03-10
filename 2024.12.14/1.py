from pathlib import Path


def list_files(path_to_file:str):
    path = Path(path_to_file)
    names = []
    for el in path.iterdir():
        names.append(el.name)
    if len(names)==0:
        return None
    return tuple(names)



    
# >>> path = r"D:\top academy\Data science\Downloads\общая литература"
# >>> list_files(path)
# ('Бхаргава. Грокаем алгоритмы.pdf', 'Макарова, Волков. Информатика.pdf', 'Таненбаум. Архитектура компьютера.pdf', 'Филиппов. Операционные системы.pdf', 'Фридл. Регулярные выражения.pdf')