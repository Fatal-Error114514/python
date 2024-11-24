from dataclasses import dataclass
from typing import Optional
@dataclass
class Node:
    val: str
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    def Insert(self, node):
        if node.val < self.val:
            if self.left:
                self.left.Insert(node)
            else:
                self.left = node
        else:
            if self.right:
                self.right.Insert(node)
            else:
                self.right = node
    def __str__(self):
        return self.val + str(self.left if self.left else '') + str(self.right if self.right else '')
m = []
while True:
    n = input()
    if n in '$*':
        m = m[::-1]
        root = Node(m[0][0])
        for i in m[1:]:
            for j in i:
                root.Insert(Node(j))
        print(str(root))
        m = []
        if n == '$':
            break
    else: m.append(n)