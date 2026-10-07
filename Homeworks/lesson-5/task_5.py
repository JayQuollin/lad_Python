"""
Звёздочка (вложенные списки / матрица). Создайте матрицу 3×4 — список из трёх строк по четыре числа. Выведите:
а) сумму всех элементов;
б) сумму элементов в каждой строке;
в) максимальный элемент во всей матрице;
г) «транспонированную» матрицу (строки и столбцы поменять местами) — разберитесь самостоятельно, как это сделать через
вложенные циклы и comprehension.
"""

def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:>4}".format(matrix[i][j]), end=" ")
        print()

matrix = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12]
]

print("Данные:")
matrix_print(matrix)

global_summ = 0
lines_summ = []
max_el = matrix[0][0]

for i in range(len(matrix)):
    line_summ = 0
    for j in range(len(matrix[i])):
        global_summ += matrix[i][j]
        line_summ += matrix[i][j]
        if matrix[i][j] > max_el:
            max_el = matrix[i][j]
    lines_summ.append(line_summ)

print(f"\nОбщая сумма: {global_summ}")
print(f"Сумма по строкам: {lines_summ}")
print(f"Максимальный элемент: {max_el}")

transp_1 = []

for j in range(len(matrix[0])):
    line = []
    for i in range(len(matrix)):
        line.append(matrix[i][j])
    transp_1.append(line)

print("\nТранспозиция циклами:")
matrix_print(transp_1)

transp_2 = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[i]))]

print("\nТранспозиция выражением:")
matrix_print(transp_2)