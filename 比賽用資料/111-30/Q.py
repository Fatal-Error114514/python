from dataclasses import dataclass

@dataclass
class Node:
    val:int
    left:int
    right:int

def depth(node, d):
    if node.left != -1 :depth(lst[node.left], d + 1)
    if node.right != -1: depth(lst[node.right], d + 1)
    depths[node.val] = d

def height(node):
    if node == -1 :return 0
    if node.left == node.right == -1:
        h[node.val] = 0
        return 0
    h[node.val] = max(height(lst.get(node.right, -1)), height(lst.get(node.left, -1))) + 1
    return h[node.val]

h = {}
depths = {}
lst = {}
p = {0:-1}
degree = {}

for _ in range(int(input())):
    m, l, r = map(int,input().split())
    tree = Node(m, r, l)
    lst[m] = tree
    p[l] = m
    p[r] = m
    degree[m] = (l != -1) + (r != -1)

height(lst[0])
depth(lst[0], 0)

for i in lst:
    print(f'node {i}: parent = {p[i]}, degree = {degree[i]}, depth = {depths[i]}, height = {h[i]},')