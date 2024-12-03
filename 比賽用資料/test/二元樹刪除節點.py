class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(edges):
    nodes = {}
    for a, b in edges:
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)
        if not nodes[a].left:
            nodes[a].left = nodes[b]
        elif not nodes[a].right:
            nodes[a].right = nodes[b]
    return nodes

def delete_node(root, target):
    if not root:
        return None
    if root.val == target:
        return None
    root.left = delete_node(root.left, target)
    root.right = delete_node(root.right, target)
    return root

def calculate_height(root):
    if not root:
        return 0
    left_height = calculate_height(root.left)
    right_height = calculate_height(root.right)
    return 1 + max(left_height, right_height)

# 主程式
edges = []
while True:
    try:
        a, b = input("輸入節點關係 (a, b)，結束輸入時按 Ctrl+D: ").split()
        edges.append((a, b))
    except EOFError:
        break

# 構建樹
nodes = build_tree(edges)
root = nodes[edges[0][0]]  # 假設第一個節點為根節點

# 輸入需要刪除的節點
target = input("請輸入要刪除的節點: ")

# 刪除指定節點
root = delete_node(root, target)

# 計算並輸出樹的高度
height = calculate_height(root)
print(f"刪除節點後的樹高: {height}")