"""
Только чётные. Вывести все чётные числа от 1 до 100 через for в сочетании с range и continue (нечётные пропускать).
"""

print("Решение через continue:")
for i in range(1, 101):
    # если при делении на 2 в остатке остается 1 - пропускать
    if i % 2:
        continue
    print(i, end=" ")

print("\nРешение через range:")
for i in range(2, 101, 2):
    print(i, end=" ")
