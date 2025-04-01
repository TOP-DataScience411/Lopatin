import re
from pathlib import Path

day = r"(?P<day>\d|(?:[12]\d|3[01]))"
month = r"(?P<month>января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)"
year = r"(?P<year>\d{4})"

#all = year+'|'+day+'|'+month

all = r'(?P<year>\d{4})|(?P<day>\d|(?:[12]\d|3[01]))|(?P<month>января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)'

pattern = re.compile(all)

text = (Path.cwd()/"history_dates_ed.txt").read_text(encoding='utf-8')

matches = pattern.findall(text,re.MULTILINE)

print(matches)


