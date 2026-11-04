from abc import ABC, abstractmethod


class Content(ABC):
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = "4.11.2026"

    @abstractmethod # обязуем всех наследников прописать этот метод
    def get_summary(self) -> str:
        """Возвращает информацию о контенте"""
        return f"Контент {self.title} создан {self.created_at}"


class Post(Content):
    def __init__(self, title: str, body: str, author: str = "Anonim") -> None:
        super().__init__(title)
        self.body = body
        self.author = author

    def get_summary(self) -> str:
        return f"Пост {self.title} создан автором {self.author}"

class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    def get_summary(self) -> str:
        line = super().get_summary()
        return f"{self.slug}: {line}"

def print_items(items: list[Content]) -> None:
    for item in items:
        print(item.get_summary())

def main() -> None:
    items = []
    print("""Меню: 
    1 - add_post
    2 - add_page
    3 - list
    0 - exit
    """)

    while True:
        to_do = input(">> ").strip()

        if to_do in ["1", "add_post"]:
            title = input("Введите название поста: ")
            body = input("Введите текст поста: ")
            items.append(Post(title=title, body=body))

        elif to_do in ["2", "add_page"]:
            title = input("Введите название страницы: ")
            slug = input("Введите slug страницы: ")
            items.append(Page(title=title, slug=slug))

        elif to_do in ["3", "list"]:
            print_items(items)

        elif to_do in ["0", "exit"]:
            break
        else:
            print("Чето как-то непонятно, попробуйте еще раз")


if __name__ == "__main__":
    main()
