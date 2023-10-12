# Напишите функцию для транспонирования матрицы

def func(lst: list) -> list:
    result = [[] for _ in lst[0]]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            result[j].append(lst[i][j])
    return result


matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
    [23, 24, 25, 26],
    [27, 28, 29, 30]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nТранспонированая матрица:")
for row in func(matrix):
    print(row)