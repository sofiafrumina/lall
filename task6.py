from collections import deque

def is_valid_move(board, row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] != '#'

def get_valid_moves(board, row, col, piece):
    if piece == 'K':
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    elif piece == 'G':
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    else:  # C - Конь
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    
    valid_moves = []
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if is_valid_move(board, new_row, new_col):
            valid_moves.append((new_row, new_col, piece))
    return valid_moves

def find_shortest_path(board):
    directions = ['K', 'G', 'C']
    paths = []
    
    # Находим начальную позицию для каждой фигуры
    for piece in directions:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == piece:
                    queue = deque([(i, j, piece, [])])  # Начинаем с каждой фигуры
                    visited = set([(i, j, piece)])  # Помечаем начальную позицию как посещенную
                    while queue:
                        row, col, piece, path = queue.popleft()
                        path.append((row, col))
                        # Проверяем, достигли ли конечной клетки
                        if board[row][col] == 'F':
                            paths.append(path)
                            break
                        # Получаем возможные ходы для текущей позиции
                        valid_moves = get_valid_moves(board, row, col, piece)
                        for move_row, move_col, next_piece in valid_moves:
                            # Проверяем, была ли уже посещена эта клетка с этой фигурой
                            if (move_row, move_col, next_piece) not in visited:
                                queue.append((move_row, move_col, next_piece, list(path)))  # Копируем путь
                                visited.add((move_row, move_col, next_piece))  # Помечаем клетку как посещенную
    if paths:
        shortest_path = min(paths, key=len)
        return len(shortest_path) - 1
    else:
        return -1

if __name__ == "__main__":
    board_size = int(input())  # Размер доски
    board = [input() for _ in range(board_size)]  # Ввод доски
    
    result = find_shortest_path(board)  # Поиск кратчайшего пути
    print(result)  # Вывод результата
