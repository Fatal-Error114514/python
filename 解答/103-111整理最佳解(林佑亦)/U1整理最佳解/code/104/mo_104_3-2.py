from sys import stdin

def Input():
    return stdin.readline().rstrip()

class NODE:
    def __init__(self, val= None):
        self.val = val
        self.left = None
        self.right = None
    
    def Insert(self, num):
        if(self.val):
            if(self.val > num):
                if(self.left):
                    self.left.Insert(num)
                else:
                    self.left = NODE(num)
            else:
                if(self.right):
                    self.right.Insert(num)
                else:
                    self.right = NODE(num)
        else:
            self.val = num
    def deep(self, count):
        global bigger
        if(self.left):
            self.left.deep(count+1)
        else:
            bigger = max(bigger,count)
        if(self.right):
            self.right.deep(count+1)
        else:
            bigger = max(bigger,count)    

node = []
for _ in range(int(Input())):
    node.append(int(Input()))

tree = NODE()
for i in node:
    tree.Insert(i)
bigger = 0
tree.deep(0)
print(bigger)
