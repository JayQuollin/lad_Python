"""
**Переопределение и `super()`.** Для `Post` переопределите `get_summary()`, **дополнив** родительскую версию через
`super()` (например, добавьте длину текста). Для `Page` — верните полностью свою реализацию. Вызовите метод у
экземпляров обоих классов и сравните вывод.
"""

from abc import ABC, abstractmethod
from datetime import date

class Content(ABC):
    def __init__(self, title: str, created_at: str = date.today().strftime("%d.%m.%Y")) -> None:
        self.title = title
        self.created_at = created_at

    @abstractmethod
    def get_summary(self):
        """Вывод информации"""
        print("Привет из родительского метода! :)")


class Post(Content):
    def __init__(self,title: str, body: str, author: str) -> None:
        super().__init__(title)
        self.body = body
        self.author = author

    def get_summary(self) -> str:
        super().get_summary()
        return f'Пост под названием "{self.title}" и содержимым [{self.body}] был создан {self.author} {self.created_at} с помощью класса Post и это хорошо'

class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    def get_summary(self) -> str:
        return f'Страница под названием "{self.title}" и слагом [{self.slug}] создана {self.created_at} с помощью класса Page и это вообще замечательно'


one = Post("Цветы", "сегодня мы разберем подвиды эхиверии", "Julia-Julia")
two = Page("Веселый садовод", "veseliy-sadovod")

print(one.get_summary()) # появится новая строка
print(two.get_summary())
