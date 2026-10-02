"""
Палиндром. Проверить, является ли строка палиндромом (читается одинаково с обеих сторон, игнорируя регистр и
пробелы/знаки). Подсказка: убрать пробелы и знаки препинания, привести к нижнему регистру, сравнить строку с её
переворотом s[::-1]. Примеры: "А роза упала на лапу Азора" → True; "Привет" → False.
"""
from unicodedata import normalize

text = "А роза упала на лапу Азора"

chars = []
for char in text:
    if char.isalpha():
        chars.append(char.lower())

normalize_text = "".join(chars)
reverse_text = normalize_text[::-1]

print(normalize_text == reverse_text)

