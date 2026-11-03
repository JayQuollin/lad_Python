"""
**«Библиотека» со классом `Book`.** Класс `Book` с `title`, `author`, `year`; методы `is_old()` (возвращает `True`,
если книга старше 10 лет) и `display()`. Атрибут класса `genre = "Художественная литература"`. Создать 3–4 книги,
вывести их и пометить «старые». Добавить атрибут класса `category_count` и объяснить в комментарии разницу между ним и
атрибутами экземпляра.
"""
from datetime import date

class Book:
    genre = "Художественная литература"
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_old(self):

        current_year = date.today().year
        if current_year - self.year > 10:
            return True
        else:
            return False

    def display(self):
        print(f'"{self.title}" - {self.author}, {self.year} год.')

really_cool_books = []
really_cool_books.append(Book("Автостопом по Галактике", "Дуглас Адамс", 1979))
really_cool_books.append(Book("Обитаемый остров", "Аркадий и Борис Стругацкие", 1969))
really_cool_books.append(Book("Записки кота Шашлыка", "Алекс Экслер", 2004))
really_cool_books.append(Book("Какая-то очень крутая не старая книга", "Современный Автор", 2020))

for book in really_cool_books:
    book.display()
    if book.is_old():
        print(">> Старая книга")
    else:
        print(">> Современная книга")

Book.category_count = 1

print(really_cool_books[0].genre)
print(really_cool_books[0].category_count)

# атрибут класса одинаковый для все экземпляров, атрибут экземпляра разны для всех экземпляров