"""
**Полиморфизм и duck typing.** Напишите функцию `render_all(items)`, которая принимает список объектов и вызывает у
каждого `get_summary()`. Заполните список постами и страницами и выведите результат. Затем **дополнительно** передайте
в неё объект, который **не** наследуется от `Content`, но имеет метод `get_summary()` (например, класс с `
__getattr__`/собственным `get_summary()`), — и покажите, что функция его тоже принимает. Это демонстрация duck typing.
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
        super().get_summary()
        return f'Пост под названием "{self.title}" и содержимым [{self.body}] был создан {self.author} {self.created_at} с помощью класса Post и это хорошо'

class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)
        self.slug = slug

    def get_summary(self) -> str:
        return f'Страница под названием "{self.title}" и слагом [{self.slug}] создана {self.created_at} с помощью класса Page и это вообще замечательно'

class SMS:
    def __init__(self, author: str, message: str) -> None:
        self.author = author
        self.message = message

    def get_summary(self) -> str:
        return f"Вам пришло СМС-сообщение от {self.author}"


def render_all(items: list) -> None:
    for item in items:
        print(item.get_summary())

contents = []
contents.append(Post("Цветы", "сегодня мы разберем подвиды эхиверии", "Julia-Julia"))
contents.append(Page("Веселый садовод", "veseliy-sadovod"))
contents.append(Post("Лучшие пляжи северной Америки", "зачем мне солнце монако", "Anastasia Moonlight"))
contents.append(SMS("Broo", "алё ты где"))


render_all(contents)