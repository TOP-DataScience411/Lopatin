from pathlib import Path
import re
from json import  dump
from urllib import request
from urllib.parse import urlparse
import chardet


def json_from_html(URL:str,re_pattern,encoding = None):
    with request.urlopen(URL) as response:
        HTML = response.read()


    if type(HTML) is bytes:
        if encoding is None:
            detected_encoding = chardet.detect(HTML)['encoding']
            encoding = detected_encoding if detected_encoding else 'utf-8'
        HTML = HTML.decode(encoding)


    if URL.endswith(".html"):
        parsed_url = urlparse(url)
        path = parsed_url.path
        filename = Path(URL).stem + ".json"
    else:
        filename = Path(__loader__.path).stem + '.json'
    cwd = Path.cwd()

    matches = re.findall(re_pattern, HTML, re.S)
    data = {key: value for key, value in matches}


    with open(filename,'w',encoding='utf-8') as json_file:
        dump(data,json_file,indent=2,ensure_ascii=False)


    return Path.cwd()/filename




url = 'https://docs.python.org/3/py-modindex.html'
modules_pattern = r'<tr>.+?>(\w+?)<.+?</td><td>.*?<em>(.*?)</em>'
file_path = json_from_html(url, modules_pattern)
print(file_path.name)


url = 'http://www.world-art.ru/cinema/rating_top.php'
films_pattern = (r'<tr .*?>'r'<td .*?<a.*?>(?P<name>.*?)</a>.*?</td>'r'<td .*?>(?P<rating>.*?)</td>')
file_path = json_from_html(url, films_pattern)
print(file_path.name)