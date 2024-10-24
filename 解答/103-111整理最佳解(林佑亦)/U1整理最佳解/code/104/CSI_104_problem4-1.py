from sys import stdin

def Input():
    return stdin.readline().rstrip()

class NODE():
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
        
    def Print(self):
        if(self.left):
            self.left.Print()
        if(self.right):
            self.right.Print()
        output.append(self.val)

for _ in range(int(Input())):
    tree = NODE()
    x = Input()
    for n in list(map(int,Input().split(','))):
        tree.Insert(n)
    output = []
    tree.Print()
    print(*output,sep=',')