# Функция для нахождения максимальной суммы очков
def max_score(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Создание двумерного массива для хранения максимальной суммы очков
    dp = [[0] * cols for _ in range(rows)]

    # Заполнение последней строки матрицы
    for j in range(cols):
        dp[rows - 1][j] = matrix[rows - 1][j]

    # Перебор строк от предпоследней до первой
    for i in range(rows - 2, -1, -1):
        # Перебор столбцов
        for j in range(cols):
            # Максимальная сумма, которую можно получить из текущей ячейки
            max_sum = 0

            # Перебор всех возможных ходов из текущей ячейки
            for k in range(max(0, j - 1), min(cols, j + 2)):
                # Если следующая ячейка содержит -1, игнорируем ее
                if matrix[i + 1][k] == -1:
                    continue
                # Выбор максимальной суммы из всех возможных ходов
                max_sum = max(max_sum, dp[i + 1][k])
            # Добавление текущего значения к максимальной сумме
            dp[i][j] = max_sum + matrix[i][j]

    # Возвращение максимальной суммы в верхнем левом углу матрицы
    return max(dp[0])

# Чтение входных данных
n = int(input())
matrix = []
for _ in range(n):
    row = input()
    matrix.append([1 if cell == 'C' else -1 if cell == 'W' else 0 for cell in row])

# Поиск и вывод максимальной суммы очков
print(max_score(matrix))
