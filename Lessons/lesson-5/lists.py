categories = []

categories.append("Python")
categories.append("Django")
categories.append("SQL")
print(categories)

categories.extend(["Git", "Docker"])
print(categories)

categories.insert(0, "Оглавление")
print(categories)

print(len(categories))

print("Docker" in categories)
print(categories.count("Git"))
print(categories.index("Docker"))

first = categories.pop(0)

print(f"Удален элемент: {first}")
print(categories)

