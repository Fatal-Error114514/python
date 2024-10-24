from sys import stdin

def Input():
    return stdin.readline().rstrip()

class NODE():
    def __init__(self, val = None):
        self.val = val
        self.l = None
        self.r = None

    def Insert(self, num):
        if(self.val):
            if(self.val > num):
                if(self.l):
                    self.l.Insert(num)
                else:
                    self.l = NODE(num)
            else:
                if(self.r):
                    self.r.Insert(num)
                else:
                    self.r = NODE(num)
        else:
            self.val = num

    def Print(self):
        if(self.l):
            self.l.Print()
        if(self.r):
            self.r.Print()
        output.append(self.val)

for _ in range(int(Input())):
    node = int(Input())
    lst = list(map(int,Input().split(',')))
    tree = NODE()
    for i in lst:
        tree.Insert(i)
    output = []
    tree.Print()
    print(*output)

