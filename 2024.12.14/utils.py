from pathlib import Path
from shutil import copy2
def load_file(path_to_file:Path):
    copy2(path_to_file,Path.cwd() / path_to_file.name)
    return Path.cwd() / path_to_file.name
