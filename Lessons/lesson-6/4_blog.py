from collections import Counter, defaultdict

posts = [
    {"title": "Введение в Python", "category": "python", "tags": ["python", "basics"]},
    {"title": "Советы по Django", "category": "django", "tags": ["django", "python", "web"]},
    {"title": "Знакомство с PostgreSQL", "category": "sql", "tags": ["sql", "postgres"]},
    {"title": "Модели Django на практике", "category": "django", "tags": ["django", "models"]},
]


def posts_printer(posts):
    for post in posts:
        print(f"[{post["category"]}] {post["title"]}")
        for tag in post["tags"]:
            print(f"#{tag}", end=" ")
        print("\n")

# posts_printer(posts)

# группировка по категориям
by_category = defaultdict(list)
for post in posts:
    by_category[post["category"]].append(post)

for category, post in by_category.items():
    print(f"Категория: {category}")
    posts_printer(post)

counts_of_tags = Counter()
for post in posts:
    counts_of_tags.update(post["tags"])

posts_printer(posts)
print(counts_of_tags)

print("\nТоп-3 тега:")
for tag, count in counts_of_tags.most_common(3):
    print(f"  {tag}: {count}")
