def print_directories(directories, indent=0):
    print('  ' * indent + directories[0])
    for directory in sorted(directories[1].keys()):
        print_directories((directory, directories[1][directory]), indent + 1)

# Чтение входных данных
n = int(input())
directories = {}

for _ in range(n):
    path = input().split('/')
    root = path[0]  # Определяем корневую директорию
    current = directories
    for directory in path[1:]:
        if directory not in current:
            current[directory] = {}
        current = current[directory]

# Вывод корневой элемента и отформатированного списка директорий
print_directories((root, directories))
