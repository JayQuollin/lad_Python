while True:
    try:
        num_1 = int(input("Введите число 1: "))
        num_2 = int(input("Введите число 2: "))
        result = num_1 // num_2
    except ZeroDivisionError:

        print("На ноль делить нельзя.")
        result = num_1 // 1

    except ValueError:
        print("Это даже не число братан...")
        continue

    else:
        print("Всё ок")
    finally:

        print(f"Результат деления: {result}")

    break
