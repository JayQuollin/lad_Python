prices = [1234, 9876, 1299, 1479, 5432]

prices.sort()
print(f"По возрастанию: {prices}")

prices.sort(reverse=True)
print(f"По убыванию: {prices}")

sorted_prices = sorted(prices)

print(f"Исходный: {prices}")
print(f"Отсортированный: {sorted_prices}")

print(f"Сумма: {sum(prices)}")
print(f"Минимальное: {min(prices)}")
print(f"Максимальное: {max(prices)}")

affordable = [num for num in sorted_prices if num <= 5000]
print(affordable)

prices_strings = [str(num) for num in sorted_prices]
print(prices_strings)


