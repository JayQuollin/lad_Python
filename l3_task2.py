secret = 7

atempt = 0

while True:
    guess = int(input("Введите число от 1 до 10: "))
    atempt +=1

    if guess < secret:
        print("Больше")
        continue
    if guess > secret:
        print("Меньше")
        continue
    print(f"Коррект! {atempt} попыток")
    break