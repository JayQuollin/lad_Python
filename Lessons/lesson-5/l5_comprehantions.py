numbers = list(range(1, 11))
squares = [num**2 for num in numbers]
print(f"Квадраты: {squares}")

evens = [num for num in numbers if num % 2 == 0]
print(f"Четные: {evens}")

prices = [1234, 9876, 1299, 1479, 5432]
flags = [num > 5000 for num in prices]

print(prices, flags, sep='\n')

categories = ['python', 'django', 'sql', 'git', 'docker']
titles = [word.capitalize() if word != 'sql' else word.upper() for word in categories]
print(titles)

