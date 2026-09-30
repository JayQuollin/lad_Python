# row_age = input("Сколько тебе лет?: ").strip()
#
# if row_age.isdigit():
#     age = int(row_age)
#     print(f"Вы ввели: {age}")
# else:
#     print("Ошибка")
#
# login = input("Логин: ").strip()
# if login and login.isalnum():
#     print(f"Логин принят: {login}")
# else:
#     print(f"Логин должен содержать буквы или цифры {login}")


full_name = input("Введите ФИО: ")
parts = full_name.split()
if len(parts) == 3:
    surname, name, milldename = parts
    print(f"Фамилия: {surname}\nИмя: {name}\nОтчество: {milldename}")
else:
    print("Введите ваше полное имя")
