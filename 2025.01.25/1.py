import re
from pathlib import Path

month = (
"январ(?:ь|я)|феврал(?:ь|я)|март?а|"
"апрел(?:ь|я)|ма[йя]|июн(?:ь|я)|июл(?:ь|я)|"
"август?а|сентябр(?:ь|я)|октябр(?:ь|я)|"
"ноябр(?:ь|я)|декабр(?:ь|я)"
)

year = r'^[12][089][0-9]{2} г\.'
year_year = r'[12][089][0-9]{2}–[12][089][0-9]{2} гг\.'
month_year = fr'^(?:{month}) [12][089][0-9]{{2}} г\.'
day_month_year = rf'^(?:[1-9]\d?) (?:{month}) [12][089][0-9]{{2}} г\.'
day_month_day_month_year = fr'^[1-9]\d? (?:{month}) – [1-9]\d? (?:{month}) [12][089][0-9]{{2}} г\.'
day_month_year_day_month_year = fr'^[1-9]\d? (?:{month}) [12][089][0-9]{{2}} г\. – [1-9]\d? (?:{month}) [12][089][0-9]{{2}} г\.'
day_day_month_year = fr'^[1-9]\d?–[1-9]\d? (?:{month}) [12][089][0-9]{{2}} г\.'
month_month_year = fr'^(?:{month})–(?:{month}) [12][089][0-9]{{2}} г\.'

pat = Path.cwd() / "history_dates_ed.txt"

with open(pat, encoding = 'utf-8') as file:
  text = file.read()

result = re.findall(day_month_year_day_month_year, text, flags = re.MULTILINE)
for res in result:
    print(res)