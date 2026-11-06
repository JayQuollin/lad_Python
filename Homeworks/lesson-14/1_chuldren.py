"""
**Базовый класс + два наследника на данных блога.** Создайте абстрактный класс `Content` с полями `title` и `created_at`
 и абстрактным методом `get_summary()`. Реализуйте наследников `Post(title, body, author)` и `Page(title, slug)` с
 `super().__init__()`. В `get_summary()` выведите краткое описание каждого.
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


class Post(Content):
    def __init__(self,title: str, body: str, author: str) -> None:
        super().__init__(title)
        self.body = body
        self.author = author

    def get_summary(self) -> str:
        return f'Пост под названием "{self.title}" и содержимым [{self.body}] был создан {self.author} {self.created_at} с помощью класса Post и это хорошо'

class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    def get_summary(self) -> str:
        return f'Страница под названием "{self.title}" и слагом [{self.slug}] создана {self.created_at} с помощью класса Page и это вообще замечательно'


one = Post("Цветы", "сегодня мы разберем подвиды эхиверии", "Julia-Julia")
two = Page("Веселый садовод", "veseliy-sadovod")

print(one.get_summary())
print(two.get_summary())