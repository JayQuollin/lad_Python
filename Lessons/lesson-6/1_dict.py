user = {
    "name": "Julia",
    "age": 27,
    "city" : "NiNo"
}

print(f"Имя: {user["name"]}")
print(f"Возраст: {user.get("age")}")
print(f"Любимая еда: {user.get('food')}")
print(f"Любимая музыка: {user.get('music', "Неизвестно")}")

print(f"\nИнформация о месте жительства: {"city" in user}")
print(f"Информация о желаемом месте жительства: {"favorite_city" in user}")

user["music"] = "Альтернативный рок"
user["name"] = "Юлия"

print(user)

old_city = user.pop("city")

print(f"\nГород удалён: {old_city}")
for key, value in user.items():
    print(f"{key}: {value}")