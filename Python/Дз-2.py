
def diagonalSort(mat):
    # Отримуємо розміри матриці
    m, n = len(mat), len(mat[0])
    
    # Словник для збереження елементів діагоналей
    diagonals = {}
    
    # Проходимо через всі елементи матриці і групуємо їх за діагоналями
    for i in range(m):
        for j in range(n):
            if i - j not in diagonals:
                diagonals[i - j] = []
            diagonals[i - j].append(mat[i][j])
    
    # Сортуємо кожну діагональ
    for diag in diagonals:
        diagonals[diag].sort()
    
    # Вставляємо відсортовані значення назад у матрицю
    for i in range(m):
        for j in range(n):
            mat[i][j] = diagonals[i - j].pop(0)
    
    return mat

matrix = [
    [5, 3, 2, 1],
    [6, 2, 1, 3],
    [3, 2, 2, 2]

]

sorted_matrix = diagonalSort(matrix)
for row in sorted_matrix:
    print(row)

def are_points_collinear(points):
    n = len(points)
    if n < 2:
        return True  # Менше 2 точок тривіально колінеарні

    # Функція для обчислення нахилу між двома точками
    def slope(x1, y1, x2, y2):
        if x2 - x1 == 0:  # Вертикальна лінія (уникнення ділення на 0)
            return float('inf')
        return (y2 - y1) / (x2 - x1)

    # Використовуємо перші дві точки для порівняння нахилів
    x1, y1 = points[0]
    x2, y2 = points[1]
    ref_slope = slope(x1, y1, x2, y2)

    # Перевіряємо нахил для кожної наступної точки
    for i in range(2, n):
        x3, y3 = points[i]
        if slope(x1, y1, x3, y3) != ref_slope:
            return False

    return True

# Приклад використання
points = [[1, 1], [2, 1], [1, 3], [1, 2]]  # Приклад координат точок
if are_points_collinear(points):
    print("All points lie on the same line.")
else:
    print("The points do not lie on the same line.")
    
def is_path_clear(king, queen, queens):
    king_x, king_y = king
    queen_x, queen_y = queen
    
    # Визначаємо крок для перевірки напрямку (0, 1, або -1)
    step_x = (queen_x - king_x) // max(1, abs(queen_x - king_x))  # 0 якщо на одній вертикалі
    step_y = (queen_y - king_y) // max(1, abs(queen_y - king_y))  # 0 якщо на одній горизонталі
    
    # Рухаємось по шляху від короля до ферзя, виключаючи самих короля та ферзя
    x, y = king_x + step_x, king_y + step_y
    while (x, y) != (queen_x, queen_y):
        if [x, y] in queens:  # Якщо інший ферзь є на шляху
            return False
        x += step_x
        y += step_y
    return True

def attacking_queens(queens, king):
    attacking = []

    for queen in queens:
        queen_x, queen_y = queen
        king_x, king_y = king
        
        # Перевірка вертикалі, горизонталі або діагоналі
        if queen_x == king_x or queen_y == king_y or abs(queen_x - king_x) == abs(queen_y - king_y):
            # Якщо шлях від короля до ферзя вільний, то додаємо цього ферзя
            if is_path_clear(king, queen, queens):
                attacking.append(queen)

    return attacking

# Приклад використання
queens = [[0, 0], [1, 1], [2, 2]]  # Масив позицій ферзів
king = [3, 3]  # Позиція короля

result = attacking_queens(queens, king)
if result:
    print("Queen(s) that can attack the king:", result)
else:
    print("No queen can attack the king.")

def dfs(grid, visited, i, j, n, m):
    # Якщо поза межами матриці або не одиниця, або вже відвідано - виходимо
    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0 or visited[i][j]:
        return 0
    
    # Відмічаємо поточний елемент як відвіданий
    visited[i][j] = True

    # Лічильник для розміру групи
    size = 1

    # Перевіряємо 4 напрямки: вгору, вниз, вліво, вправо
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        new_i, new_j = i + direction[0], j + direction[1]
        size += dfs(grid, visited, new_i, new_j, n, m)

    return size

def largest_connected_group(grid):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    
    # Створюємо масив відвіданих елементів
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_group_size = 0

    # Перебираємо кожен елемент матриці
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                # Знаходимо розмір нової групи одиниць
                group_size = dfs(grid, visited, i, j, n, m)
                max_group_size = max(max_group_size, group_size)

    return max_group_size

# Приклад використання
grid = [
    [1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1]
]

print("Largest island: ", largest_connected_group(grid))
