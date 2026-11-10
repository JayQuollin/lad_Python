"""
Агрегация «баллы за курс». Дан словарь scores с баллами по курсам (не менее 4 курсов). Напишите цикл по items(), который:

выведет каждую пару в формате курс: балл;
посчитает сумму баллов;
через get() выведет значение для курса, которого в словаре нет, с запасным текстом.
"""

scores = {
    "python": 90,
    "django": 75,
    "postgres": 60,
    "SQL": 66
}

summ = 0
for name, score in scores.items():
    print(f"{name}: {score}")
    summ += score

print(f"Всего баллов: {summ}")

new_course = "C++"
print(f"Баллы за курс {new_course}: {scores.get(new_course, "Курс отсутствует")}")
