"""
Dict comprehension + Counter. Для списка слов words:

постройте словарь {слово: длина} через dict comprehension;
посчитайте частоту встречаемости слов через Counter;
выведите топ-3 самых частых слова через most_common(3).
"""

from collections import Counter

words = ["python", "django", "web", "api", "python", "python", "api", "flask", "sql"]

lengh_dict = {word : len(word) for word in words}
print(lengh_dict)

frec = Counter(words)
print(frec)

print(f"TOP-3 MOST POPULAR: {frec.most_common(3)}")
