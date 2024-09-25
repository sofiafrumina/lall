# Чтение входных данных
n, direction = input().split()
n = int(n)
matrix = [list(map(int, input().split())) for _ in range(n)]

# Определение направления поворота
clockwise = (direction == 'R')

# Генерация и вывод операций
operations = []
for i in range(n):
    for j in range(i, n - i - 1):
        if clockwise:
            operations.append((i, j, j, n - 1 - i))
            operations.append((i, j, n - 1 - i, n - 1 - j))
            operations.append((i, j, n - 1 - j, i))
        else:
            operations.append((i, j, n - 1 - j, i))
            operations.append((i, j, n - 1 - i, n - 1 - j))
            operations.append((i, j, j, n - 1 - i))

print(len(operations))
for operation in operations:
    print(*operation)

