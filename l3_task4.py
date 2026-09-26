posts = [
    "Скозь кротовую нору",
    "Пульсирующая вселенная",
    "Занимательная астрономия",
]
print("Свежие статьи")

for num, title in enumerate(posts, start=1):
    print(f"{num + 1}. {title}")

print("\nКарточка статьи")
for title in posts:
    print(f"{title} - {len(title)} символов")

print("\nПоиск")

if "Пульсирующая вселенная" in posts:
    print("Найдено")
else:
    print("Не найдено")