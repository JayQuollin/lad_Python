"""
Красивый заголовок. На вход подаётся «грязный» заголовок с лишними пробелами, кавычками и знаками препинания.
«Почистить» его: убрать краевые пробелы (strip), схлопнуть повторные пробелы (split + join), снять фигурные
скобки/кавычки (replace) и перевести каждое слово с заглавной буквы (capitalize в цикле). Вывести аккуратный заголовок.

"""


dirty_title = " Gorillaz     - 'Dirty Harry' {Official video}   "
print(f"Оригинал: {dirty_title}")

data = dirty_title.strip()
print(f"strip: {data}")

data = " ".join(data.split())
print(f"split + join: {data}")

while "{" in data:
    data = data.replace("{", "")
while "}" in data:
    data = data.replace("}", "")
while '"' in data:
    data = data.replace('"', "")
while "'" in data:
    data = data.replace("'", "")
print(f"replace: {data}")

data = data.split()
clean_title = []

for word in data:
    clean_title.append(word.capitalize())

clean_title = " ".join(clean_title)
print(f"capitalize: {clean_title}")
