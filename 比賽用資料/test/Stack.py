class Stack():
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def get(self):
        return self.stack[self.size()-1]
    
    def cls(self):
        self.stack=[]

    def empty(self):
        return self.stack==[]
    
stack=Stack()

for i in "ABC":
    stack.push(i)
    print(f"將{i}放入堆疊")
stack.cls()
"""for i in range(3):
    print(f"堆疊取出{stack.get()}，同時不刪除")"""
while not stack.empty(): #list裡面有資料就進迴圈
    print(stack.pop())
print("程式結束")