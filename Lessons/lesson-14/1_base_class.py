from typing import override


class Content:
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = "4.11.2026"

    def get_summary(self) -> str:
        return f"Контент {self.title} создан {self.created_at}"


class Post(Content):
    def __init__(self, title: str, body: str, author: str) -> None:
        super().__init__(title)
        self.body = body
        self.author = author

    @override
    def get_summary(self) -> str:
        return f"Пост {self.title} создан {self.created_at} автором {self.author}"

class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    @override
    def get_summary(self) -> str:
        line = super().get_summary()
        return f"{self.slug}: {line}"

my_post = Post(title="Математика", body="2+2", author="Марина")
my_page = Page(title="Учебники", slug="this-school")

# print(f"{my_post.title}: {my_post.created_at}, {my_post.author}")
# print(f"{my_page.title}: {my_page.created_at}, {my_page.slug}")

print(my_post.get_summary())
print(my_page.get_summary())
print(Post.__mro__)

