from unicodedata import normalize

text = "Занимательная    алгебра  и   геометрия"
words = text.split()

print(words)

print(f"Слов в тексте: {len(words)}")

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Самое длинное слово - {longest}")

new_text = " | ".join(words)
print(new_text)

normalized = " ".join(text.split())
print(normalized)

print(f"Первая строка: {len(text)}, последняя строк: {len(normalized)}")