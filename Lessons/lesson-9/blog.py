import time
import functools

articles = [
    {"id": 1, "title": "Матрешки", "author": "Julia"},
    {"id": 2, "title": "Слишком много врапперов", "author": "Максим"},
    {"id": 3, "title": "Еще больше про декораторы", "author": "Иван"},
]

def time_it(func):
    @functools.wraps(func) # декоратор для декоратора
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} отработала за: {elapsed:.6f} с.")
        return result
    return wrapper

def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов: {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Результат: {func.__name__} == {result}\n\n")
        return result
    return wrapper

@logged
@time_it
def list_articles() -> str:
    for post in articles:
        print(f"[{post["id"]}] {post["author"]}: {post["title"]}")

    return f"Всего статей: {len(articles)}"

@logged
def add_article(title: str, author: str) -> str:
    new_id = max(post["id"] for post in articles) + 1
    new_article = {"id": new_id, "title": title, "author": author}
    articles.append(new_article)
    return f"Добавлена статься [{new_id}]"

@logged
def find_article(article_id: int) -> str | None:
    for post in articles:
        if post["id"] == article_id:
            return post["title"]
    return None

list_articles()
add_article(title="Куда почти все делись", author="NoName")
list_articles()

find_article(3)