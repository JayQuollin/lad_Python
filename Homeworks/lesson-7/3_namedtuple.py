"""Каталог статей (namedtuple). Определить Post с полями title, category, year. Создать список из 4 статей.
Реализовать:
1. вывести все стать
2. отсортировать по году по убыванию
3. найти и вывести статьи заданной категории,
4. добавить новую статью. Оформить вывод через f-строки.

**Группировка по категории.** Для того же каталога статей сгруппировать заголовки по категории с помощью `defaultdict` 
из `collections`, а затем посчитать количество статей в каждой категории через `Counter`. Вывести оба результата.

"""


from collections import namedtuple, defaultdict, Counter

Post = namedtuple("Post", ["title", "category", "year"])

def posts_print(data: list[Post]) -> None:
    for post in data:
        print(f"[{post.year}][{post.category}]: {post.title}")


data = [

    Post("Ележивика", "ягоды", 2024),
    Post("Клубника", "ягоды", 2014),
    Post("Розовая гитара", "музыка", 2025),
    Post("Короче, анегдот", "анегдоты", 2016)

]

print("Все статьи:")
posts_print(data)

print("\nГод по убыванию:")
posts_print(sorted(data, key=lambda post: post.year, reverse=True))

this_category = "ягоды"
print(f"\nВсё из категории [{this_category}]:")
posts_print([post for post in data if post.category==this_category])

title = "Что такое спать"
category = "Учеба"
year = 2026
data.append(Post(title, category, year))

print("\nВсе статьи:")
posts_print(data)

categories_data = defaultdict(list)
for post in data:
    categories_data[post.category].append([post.title, post.year])

print(f"\nКак выглядит defaultdict: \n{categories_data}\n")

counter = Counter([post.category for post in data])
print(f"\nКак выглядит counter: \n{counter}\n")

for name, q in counter.items():
    print(f"{name}: {q}")





