total = 0
for number in range(1, 6):
    cube = number ** 3
    print(f"{number} в кубе = {cube}")
    total += cube

print(f"Сумма всех кубов: {total}")