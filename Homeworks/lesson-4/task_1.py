"""
Счётчик слов. Дана строка с текстом поста. Разбить её на слова через split(), вывести количество слов и первое слово в
верхнем регистре (upper()).
"""

text = """
Admire me, admire my home
Admire my son, he's my clone
Yeah, yeah, yeah, yeah
This land is mine, this land is free
I'll do what I want but irresponsibly
It's evolution, baby
"""

data = text.split()

print(len(data))
print(data[0].upper())
