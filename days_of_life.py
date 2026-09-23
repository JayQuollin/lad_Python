
while True:
    years = input("Введите количество лет: ")
    try:
        years = int(years)
        print("понял")
        break
    except ValueError:
        print("непонял")

days = years * 365

print(f"{years} лет это {days} дней")
