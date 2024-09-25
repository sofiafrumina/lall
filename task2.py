def rotate_matrix_in_place(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Создаем новую матрицу для поворота
    rotated_matrix = [[0] * n for _ in range(m)]

    # Транспонирование матрицы и запись в новую матрицу
    for i in range(n):
        for j in range(m):
            rotated_matrix[j][n - i - 1] = matrix[i][j]

    # Вывод повернутой матрицы
    for row in rotated_matrix:
        print(*row)

# Чтение размеров матрицы
n, m = map(int, input().split())

# Чтение матрицы
matrix = [list(map(int, input().split())) for _ in range(n)]

# Поворот матрицы на месте и вывод результата
rotate_matrix_in_place(matrix)
