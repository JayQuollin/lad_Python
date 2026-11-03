"""
⭐ Словарь с defaultdict. Дан список кортежей [(имя, предмет, оценка), ...]. Используя defaultdict(list), сгруппируйте
оценки по именам студентов, а затем через defaultdict(list) или Counter выведите для каждого студента список его
предметов и средний балл. (Подумайте: как посчитать средний балл, имея список оценок?)
"""

from collections import Counter, defaultdict

data = [

    ("Павел", "Алгебра", "5"),
    ("Мария", "Геометрия", "4"),
    ("Алексей", "Алгебра", "4"),
    ("Екатерина", "Алгебра", "5"),
    ("Юлия", "Геометрия", "5"),
    ("Анна", "Русский Язык", "5"),
    ("Павел", "Русский Язык", "3"),
    ("Алексей", "Русский Язык", "3"),
    ("Екатерина", "Русский Язык", "5"),
    ("Юлия", "Алгебра", "4"),

]

result = defaultdict(list)

# создание конструкции Имя: [(предмет_1, оценка), (предмет_2, оценка) ...]
for line in data:
    result[line[0]].append((line[1], line[2]))


# вывод
for name, grads in result.items():
    print(f"\n{name}:")
    for grade in grads:
        print(f"{grade[0]} - {grade[1]}")

# средний балл
print("\nСредний балл:")
for name, grads in result.items():
    summ = 0
    for grade in grads:
        summ += int(grade[1])
    print(f"{name}: {summ / len(grads)}")

