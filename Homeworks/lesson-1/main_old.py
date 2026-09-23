"""
Задание 1 - main.py
Задание 2 - facts_and_types.py
Задание 3 - days_of_life.py
Задание 4 - main.py, days_of_life.py
"""



name = input("Имя: ")

try:
    age = int(input("Возраст: "))
    print(f"Привет, {name}! Рад слышать что тебе уже {age} лет!")
except ValueError:
    print(f"Привет, {name}! К сожалению я не понял сколько тебе лет :c")