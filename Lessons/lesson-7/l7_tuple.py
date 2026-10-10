point = (10, 20)
color = "red", "green", "blue"

single = (5,)

print(type(single))

not_tuple = (5)
print(type(not_tuple))

print(len(color))

print(color[0])
print(color[-1])
print(color[1:])

print("red" in color)

if "green" in color:
    print(f"Индекс зеленого: {color.index("green")}")

print(f"Количество красного: {color.count("red")}")

try:
    color[0] = "yellow"
except TypeError as err:
    print(f"Нельзя изменить кортеж: {err}")


