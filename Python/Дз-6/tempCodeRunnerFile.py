class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.left = None
        self.right = None

def add_node(root, id, value, left, right):
    if root is None:
        root = Node(id, value)
    if left is not None:
        root.left = Node(left[0], left[1])
    if right is not None:
        root.right = Node(right[0], right[1])
    return root

def find_max_sum_path(root):
    def dfs(node, current_path, current_sum):
        if node is None:
            return ([], 0)
        current_path.append(node.id)
        current_sum += node.value
        if node.left is None and node.right is None:  # Листок
            return (current_path[:], current_sum)
        left_path, left_sum = dfs(node.left, current_path, current_sum)
        right_path, right_sum = dfs(node.right, current_path, current_sum)
        current_path.pop()  # Видаляємо поточну вершину з шляху
        return (left_path, left_sum) if left_sum > right_sum else (right_path, right_sum)
    
    max_path, max_sum = dfs(root, [], 0)
    return max_path, max_sum

# Побудова дерева через консоль
n = int(input("Введіть кількість вершин: "))
nodes = {}

for _ in range(n):
    data = input("Введіть id вершини, value, left id і right id (якщо немає, то -1): ").split()
    id, value = int(data[0]), int(data[1])
    left = (int(data[2]), int(data[2])) if data[2] != '-1' else None
    right = (int(data[3]), int(data[3])) if data[3] != '-1' else None
    
    if id not in nodes:
        nodes[id] = Node(id, value)
    node = nodes[id]
    if left:
        nodes[left[0]] = Node(left[0], left[1])
        node.left = nodes[left[0]]
    if right:
        nodes[right[0]] = Node(right[0], right[1])
        node.right = nodes[right[0]]

# Знаходження шляху з найбільшою сумою
root_id = int(input("Введіть id кореня: "))
root = nodes[root_id]
max_path, max_sum = find_max_sum_path(root)
print("Шлях з найбільшою сумою значень:", max_path)
print("Сума значень:", max_sum)
