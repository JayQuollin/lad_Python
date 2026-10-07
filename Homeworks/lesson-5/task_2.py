"""
Фильтрация строк через comprehension. Заведите список из 8–10 строк (например, названий категорий блога). Через list
comprehension: а) отфильтруйте строки длиннее 5 символов; б) постройте список из длин всех строк (len); в) постройте
список строк с первой буквой в верхнем регистре (capitalize()). Выведите каждый результат.
"""

groups = [
    "ДДТ",
    "Дайте танк!",
    "[AMATORY]",
    "Алиса",
    "Сплин",
    "Король и шут",
    "Nautilus Pompilius",
    "7Раса",
    "сглаз"
]

print("Данные:", groups)

more_then_five = [name for name in groups if len(name) > 5]
print("A) Группы, длиннее 5: ", more_then_five)

lens_list = [len(name) for name in groups]
print("Б) Длины: ", lens_list)

norm_start = [name for name in groups if name[0].isalpha() and name[0] == name[0].capitalize()]
print("В) Строки с нормальным началом:", norm_start)