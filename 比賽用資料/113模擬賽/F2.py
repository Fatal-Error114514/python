class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
    
    def Insert(self, node):
        if self.val:
            if node < self.val:
                if self.left:
                    self.left.Insert(node)
                else:
                    self.left = Node(node)
            else:
                if self.right:
                    self.right.Insert(node)
                else:
                    self.right = Node(node)
        else:
            self.val = node
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
                root.Insert(j)
        print(str(root))
        m = []
        if n == '$':
            break
    else: m.append(n)