from pathlib import Path
from PyPDF2 import PdfReader
import re
import pickle




def find_Morozoff():
    path = Path.cwd().parents[1]
    name = "Морозов. Проверка статистических гипотез.pdf"
    found_files = list(path.glob(f"**/{name}"))
    if not found_files:
        raise FileNotFoundError(f"Файл {name} не найден в {path}")
    return found_files[0]

def extract_numbers(text):

    cleaned_text = re.sub(r'(\d)\s+(\d)', r'\1\2', text)
    return [int(num) for num in re.findall(r'\d+', cleaned_text)]


def get_data(file_path):

    pattern = re.compile(
        r"Вариант\s+(?P<variant>\d+)\.\s*"
        r"N:\s*(?P<N>[\d,\s]+?);\s*"
        r"R:\s*(?P<R>[\d,\s]+?)(?:\.|$)"
    )

    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        text = "\n".join(page.extract_text() for page in reader.pages)

    matches = pattern.finditer(text)

    results = []
    for match in matches:
        n_tasks = [num.strip() for num in match.group('N').split(",") if num.strip()]
        r_tasks = [num.strip() for num in match.group('R').split(",") if num.strip()]

        results.append({
            'variant': int(match.group('variant')),
            'N': extract_numbers(match.group('N')),
            'R': extract_numbers(match.group('R'))
        })

    return results


def fixproblem(data):
    data[3]['R'].remove(10321112)
    data[3]['R'].extend([1032,1112])

    return data

def save_instance(data):
    with open("data.pic",'wb') as file:
        pickle.dump(data,file)

def load_pic_instance():
    with open("data.pic",'rb')as file:
        data = pickle.load(file)
    return data

def check_first_and_last(element:str,N):
    print(f'''
    математическое ожидание {element}   Mn = {N.mean()}
                    дисперсия {element} Dn = {N.std()**2}
    квадратическое отклонение {element} rn = {N.std()}
    ''')
    r = np.abs(N[-1]-N.mean())/(N.std()*np.sqrt((len(N)-1)/len(N)))
    print(f'''
    Вычисляем характеристику r по формуле : r = {r}
    ''')
    t_critical = t.ppf(1 - level_of_significance/2, df=(len(N)-2))
    print(f'''
    По таблице приложения Д находим для числа степеней свободы 
     {len(N)-2} критическое значение r = {t_critical}.
    ''')
    if r < t_critical:
        print(f'''
        Поскольку r = {r} < {t_critical}, то нулевая гипотеза принимается, и 
    последний член ряда {element} не является промахом.
        ''')
    else:print(f'''
    Поскольку r = {r} > {t_critical}, то нулевая гипотеза опровергается, и 
    последний член ряда {element} является промахом.
    ''')
    r = np.abs(N[0]-N.mean())/(N.std()*np.sqrt((len(N)-1)/len(N)))
    print(f'''
    Выдвигаем нулевую гипотезу, что первый член вариационного ряда 
    {element} (
    N1 = {N[0]} кH) принадлежит генеральной совокупности.
    Вычисляем характеристику r по формуле r = {r}
    ''')

    if r < t_critical:
        print(f'''
        Поскольку r = {r} < {t_critical}, то нулевая гипотеза принимается, и 
    первый член ряда {element} не является промахом.
        ''')
    else:print(f'''
    Поскольку r = {r} > {t_critical}, то нулевая гипотеза опровергается, и 
    первый член ряда {element} является промахом.''')


