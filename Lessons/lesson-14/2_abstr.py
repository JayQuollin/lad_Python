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
    def __init__(self, title: str, body: str, author: str) -> None:
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

def show(item: Content) -> None:
    print(item.get_summary())

my_post = Post(title="Математика", body="2+2", author="Марина")
my_page = Page(title="Учебники", slug="this-school")

print(my_post.get_summary())

items = [my_post, my_page]
for item in items:
    show(item)

