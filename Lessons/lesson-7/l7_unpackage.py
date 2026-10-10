point = (10, 20)

x, y = point
print(x, y)

firs, *rest = (10, 20, 30, 40)
print(firs, rest)

a, b = 1, 2
a, b = b, a

print(f"a = {a}, b = {b}")

pairs = [("name", "Julia"), ("age", 20)]
for key, value in pairs:
    print(f"{key}: {value}")