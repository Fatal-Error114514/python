from sys import stdin

def Input():
    return stdin.readline().strip()

class NODE():
    def __init__(self, val = None):
        self.l = None
        self.r = None
        self.val = val

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

    def Do(self, num):
        output.append(self.val)
        if(self.val > num):
            self.l.Do(num)
        elif(self.val < num):
            self.r.Do(num)
        else:
            return 

    def Hight(self, hight = 1):
        global bigger
        if(self.l):
            self.l.Hight(hight +1)
        if(self.r):
            self.r.Hight(hight +1)
        bigger = max(hight, bigger)

output = []
bigger = 0
n,m = map(int,Input().split(','))
lst = list(map(int,Input().split()))
tree = NODE()
if(m in lst):
    for i in lst:
        tree.Insert(i)
    tree.Do(m)
    tree.Hight()
    print(len(output))
    print(bigger)
    print(*output, sep='>')
else:
    print('Not found.')
