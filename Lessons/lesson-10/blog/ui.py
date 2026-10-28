from rich.comsole import Console
from rich.table import Table
from blog import data

console = Console()

def create_post_menu() -> None:
     title = input("Название: ")
     author = input("Автор: ")
     text = input("Текст: ")
     data.create_post(title, author, text)
     console.print(f"[green]Статья {title} сохранена успешно.[/green]")

def show_posts_menu() -> None:
    posts = data.list_posts()
    if not posts:
        console.print("[yellow]Статей пока нет.[\yellow]")
        return

    # for post in posts:
    #     print(f" * {post["title"]} [{post["author"]}]: {post['text']}")

    table = Table(title="Статьи блога:")
    table.add_column("Заголовок")
    table.add_column("Автор")
    table.add_column("Текст")
    for post in posts:
        table.add_row(post["title"], post["author"], post["text"])
    console.print(table)

if __name__ == "__main__":
    print("Я работаю!")