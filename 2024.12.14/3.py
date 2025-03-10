from pathlib import Path
from utils import load_file
from importlib.util import spec_from_file_location , module_from_spec

def ask_for_file():
    while True:
        path_to_file = Path(input("Введите путь к файлу: "))
        if path_to_file.exists():break
        print("Неверный путь к файлу")

    spec = spec_from_file_location("my_module",load_file(path_to_file))

    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    return module

# >>> module = ask_for_file()
# Введите путь к файлу: D:\top academy\Data science\Homework\2024.12.14\data\conf.py
# >>> module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
# >>>