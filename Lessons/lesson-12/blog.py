import json
import logging
from pathlib import Path
from validation import ValidationError
from l12_finally import POSTS_FILE

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
)

my_logger = logging.getLogger("blog")


def load_posts() -> list:
    if not POSTS_FILE.exists():
        my_logger.info(f"Файл {POSTS_FILE} не найден. Возвращаем пустой список.")
        return []

    try:
        with POSTS_FILE.open(encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as err:
        my_logger.error(f"Не могу декодировать файл {POSTS_FILE}, ошибка {err}")
        raise

def save_posts(posts: list) -> None:
    with POSTS_FILE.open(mode="w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)
    my_logger.info(f"Записано {len(posts)} постов.")

def add_post(title: str, body: str) -> dict:
    if not title or not body:
        raise ValidationError("Не должно быть пустых полей!")

    posts = load_posts()
    post = {"title": title, "body": body }
    posts.append(post)
    save_posts(posts)
    return post

def list_posts() -> None:
    posts = load_posts()
    if not posts:
        print("Нет постов.")
        return
    for num, post in enumerate(posts, start=1):
        try:
            print(f"[{num}] {post['title']}: {post['body']}")
        except KeyError as err:
            my_logger.error(f"В файле {POSTS_FILE} неправильная структура данных, {err}")
            print("Некорректный файл.")
            break

if __name__ == "__main__":
    my_logger.info("Программа начала работу.")
    while True:
        print("""Выберите действие:
add -> Добавить пост
list -> Показать все посты
exit -> Выход
""")
        action = input("> ").strip().lower()
        if action == "add":
            title = input("Введите название: ").strip()
            body = input("Введите текст поста: ").strip()
            try:
                add_post(title, body)
            except ValidationError as err:
                my_logger.warning(f"Некорректный ввод, ошибка {err}")
                print(f"Ошибка, попробуйте еще раз. \n{err} ")

            except json.JSONDecodeError:
                print(f"Файл поврежден.")

            else:
                print("Пост добавлен успешно.")

        elif action == "list":
            try:
                list_posts()
            except json.JSONDecodeError:
                print(f"Файл поврежден.")
        elif action == "exit":
            my_logger.info("Программа завершила работу.")
            print("Завершение работы...")
            break
        else:
            print("Неизвестная команда, попробуйте снова.")

