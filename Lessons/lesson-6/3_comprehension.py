from collections import Counter

# квадраты нечетных чисел:
odd_squares = {x: x**2 for x in range(10) if x % 2}
print(odd_squares)

# длины слов
words = ["python", "django", "web", "api", "python", "python", "api", "flask", "sql"]
lenghts = {word: len(word) for word in words}
print(lenghts)

# подсчет частоты слов:
count = Counter(words)
print(count)
print(count.most_common(3))

print(Counter("Привет, мир!"))