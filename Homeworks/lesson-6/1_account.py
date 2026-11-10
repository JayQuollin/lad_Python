"""
1. Словарь «профиль». Создайте словарь с данными пользователя (имя, возраст, город, профессия). Затем:
 - выведите значение по ключу и через get() с запасным значением;
 - проверьте через in, есть ли в словаре ключ "phone";
 - добавьте ключ "email" и измените значение "age";
 - удалите один ключ через pop и выведите получившийся словарь.
"""

account = {
    "name": "Julia",
    "age" : 17,
    "city": "NiNo",
    "prof": "Robomaker"
}

print(f"""
Такой ключ есть: {account["name"]}
И такой есть: {account.get("age")}
А такого уже нет: {account.get("town", "Error")}
""")

print(f"Информация о городе: {"city" in account}")
print(f"Информация о телефоне: {"phone" in account}")

account["email"] = "julia-julia@mail.ru"
account["age"] = 27

account.pop("prof")

for key, value in account.items():
    print(f"{key}: {value}")
