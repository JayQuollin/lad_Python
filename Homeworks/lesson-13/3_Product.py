"""
 **«Товар и корзина».** Класс `Product` (`title`, `price`, `quantity`) с методом `total_price()` (цена × количество).
 Класс `Cart`, который хранит список продуктов и методы `add(product)`, `total_sum()` и `show()`. Добавить несколько
 товаров, вывести общую сумму.
"""

class Product:
    def __init__(self, title, prise, quantity):
        self.title = title
        self.prise = prise
        self.quantity = quantity

    def total_prise(self):
        return self.prise * self.quantity


class Cart:
    def __init__(self):
        self.backet = []

    def add(self, product):
        self.backet.append(product)

    def total_sum(self):
        summ = 0
        for prod in self.backet:
            summ += prod.total_prise()
        return summ

    def show(self):
        print("{:-^45}".format('ЧЕК'))
        for prod in self.backet:
            # print(line = f"{prod.title:<20}{prod.total_prise:>10}")
            left_text = f"{prod.title} {prod.prise} руб. х {prod.quantity} шт."
            right_text = prod.total_prise()
            line = f"{left_text:<35}{right_text:>10}"
            print(line)

        left_text = "Итог:"
        right_text = self.total_sum()
        line = f"{left_text:<35}{right_text:>10}"
        print("{: ^45}".format('---'))
        print(line)
        print("{:-^45}".format('Спасибо за покупку!'))

Guitar = Product("Гитара", 20000, 1)
Beer = Product("Пиво", 90, 4)
Tires = Product("Зимняя резина", 36000, 1)
Insurance = Product("ОСАГО", 22000, 1)

Sanyas_backet = Cart()
Sanyas_backet.add(Guitar)
Sanyas_backet.add(Beer)
Sanyas_backet.add(Tires)
Sanyas_backet.show()
