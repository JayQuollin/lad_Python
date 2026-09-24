age = int(input("Введите возраст: "))

if 0 >= age >= 12:
    print("Ребенок")
elif 13 <= age <= 17:
    print("Подросток")
elif 18 <= age <= 64:
    print("Взрослый")
elif 65 <= age <= 150:
    print("Пенсионер")
else:
    print("Некорректные данные")
    