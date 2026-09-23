
years = input("Введите количество лет: ")

while True:
    try:
        years = int(years)
        break
    except ValueError:
        years = input("Введите количество лет ЧИСЛОМ пожалуйста: ")

days = years * 365

print(f"{years} лет это {days} дней")