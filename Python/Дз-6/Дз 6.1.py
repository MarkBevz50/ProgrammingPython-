class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.left = None
        self.right = None

def add_node(nodes, visited, id, value, left_id, right_id):
    # Перевірка на зациклення
    if id in visited:
        raise ValueError("Зациклення дерева: це не дерево, а граф.")

    # Додаємо поточний вузол до відвіданих
    visited.add(id)
    
    # Створення вузла, якщо він ще не існує
    if id not in nodes:
        nodes[id] = Node(id, value)
    else:
        nodes[id].value = value

    # Додавання лівого нащадка
    if left_id != "none":
        if left_id in visited:
            raise ValueError("Зациклення дерева: це не дерево, а граф.")
        if left_id not in nodes:
            nodes[left_id] = Node(left_id, 0)
        nodes[id].left = nodes[left_id]

    # Додавання правого нащадка
    if right_id != "none":
        if right_id in visited:
            raise ValueError("Зациклення дерева: це не дерево, а граф.")
        if right_id not in nodes:
            nodes[right_id] = Node(right_id, 0)
        nodes[id].right = nodes[right_id]

def find_max_sum_path(root):
    def dfs(node):
        if node is None:
            return [], 0  # Порожній шлях і сума 0
        
        # Отримуємо шляхи та суми для лівого і правого піддерев
        left_path, left_sum = dfs(node.left)
        right_path, right_sum = dfs(node.right)
        
        # Вибираємо шлях з найбільшою сумою
        if left_sum > right_sum:
            max_path = [node.id] + left_path
            max_sum = node.value + left_sum
        else:
            max_path = [node.id] + right_path
            max_sum = node.value + right_sum
        
        return max_path, max_sum

    max_path, max_sum = dfs(root)
    return max_path, max_sum

# Основна частина програми для введення даних
n = int(input("Введіть кількість вершин: "))
nodes = {}
visited = set()  # Множина для відстеження відвіданих вершин

for _ in range(n):
    while True:
        try:
            data = input("Введіть id вершини, value, left id і right id (якщо немає, то 'none'): ").split()
            if len(data) != 4:
                raise ValueError("Необхідно ввести рівно 4 значення.")
            id = int(data[0])
            value = int(data[1])
            left_id = data[2] if data[2].lower() == "none" else int(data[2])
            right_id = data[3] if data[3].lower() == "none" else int(data[3])
            add_node(nodes, visited, id, value, left_id, right_id)
            break  # Вихід з циклу, якщо дані введені коректно
        except ValueError as e:
            print(f"Помилка вводу: {e}. Спробуйте ще раз.")

root_id = int(input("Введіть id кореня: "))
if root_id in nodes:
    root = nodes[root_id]
    max_path, max_sum = find_max_sum_path(root)
    print("Шлях з найбільшою сумою значень:", max_path)
    print("Сума значень:", max_sum)
else:
    print("Кореня з вказаним id не знайдено.")
