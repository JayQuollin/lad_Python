"""
Поиск по блогу. Есть список заголовков постов. Вывести только те, что содержат слово "Python" (через find или in).
Затем для каждого заголовка вывести его slug через написанную на занятии функцию build_slug.
"""

def build_slug(title: str) -> str:
    result = title.lower()
    result = result.replace(" ", "-")

    clean = []
    for char in result:
        if char.isalnum() or char == "-":
            clean.append(char)
        else:
            clean.append("-")

    result = "".join(clean)

    while "--" in result:
        result = result.replace("--", "-")

    result = result.strip("-")
    return result


titles = [
    "Python is a capital of Great Britain",
    "Изучение Python, С++, С# во сне без sms и регистрации (Методика Филиппа Акимова)",
    "О чем говорят слова паразиты",
    "Что такое slug в Python и при чем тут наковальня?",
    "Овощи, богатые витамином С",
    "333 рецепта шарлотки",
    "All about Monty Python"
]

for title in titles:
    if "Python" in title:
        print(title)

print("\nSlugs:")
for title in titles:
    print(build_slug(title))