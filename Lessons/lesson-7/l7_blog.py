from collections import namedtuple

from unicodedata import category

Post = namedtuple("Post", ["title", "category", "year"])

posts = [
    Post("Модели Django", "IT", 2025),
    Post("Индексы в PostgreSQL", "DB", 2024),
    Post("View-функции", "Django", 2026),
    Post("Транзакции", "DB", 2025)
]

posts.append(Post("Формы и валидация", "Django", 2026))

print("Все статьи:")

for post in posts:
    print(f"[{post.year}] [{post.category}]: {post.title}")


sorted_posts = sorted(posts, key=lambda post: post.year)

print("\nСтатьи по годам:")
for post in sorted_posts:
    print(f"[{post.year}] [{post.category}]: {post.title}")

category = "DB"

matching = [post for post in posts if post.category == category]

print(f"\nСтатьи по категории: {category}")
for post in matching:
    print(f"[{post.year}] [{post.category}]: {post.title}")

number = 37
even_or_odd = "odd" if number % 2 else "even"
print(even_or_odd)


odd_or_even = ["even", "odd"][number % 2]
print(odd_or_even)
