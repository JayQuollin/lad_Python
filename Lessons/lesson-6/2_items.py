scores = {
    "python": 90,
    "django": 75,
    "postgres": 60,
}

# перебор по ключам
for line in scores:
    print(line)

# по значениям:
for value in scores.values():
    print(value)

# по парам:
for key, value in scores.items():
    print(f"{key}: {value}")

total = 0
for value in scores.values():
    total += value
print(f"Общее количество баллов: {total}")


print(scores.get("flask", "Курс отсутствует"))