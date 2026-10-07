"""
Цены и «доступность». Дан список цен. Порог вводится с клавиатуры. Через comprehension постройте список флагов
True/False — цена меньше порога. Посчитайте, сколько цен ниже порога (sum(flags)), и выведите среднюю цену только по
«доступным» позициям.
"""

prices = [146.99, 1499, 2599, 79.99, 10200, 3550]
print(prices)
filter = float(input("Порог: "))

analised_prices = [True if price <= filter else False for price in prices]
print(analised_prices)

quantity = sum(analised_prices)
print(f"Количество доступных позиций: {quantity}")

summ = 0
for i in range(len(prices)):
    if analised_prices[i]:
        summ += prices[i]

print(f"Средняя цена: {summ/quantity}")