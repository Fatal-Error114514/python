class Queue():  
    """佇列"""
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,data):
        """data插入佇列"""
        self.queue.insert(0,data)
        return data
    def size(self):
        """回傳佇列長度"""
        return len(self.queue)
    def dequeue(self):
        if len(self.queue):
            return self.queue.pop() #pop默認刪除最後一個值
        return "佇列是空的"
q=Queue()
print("已成功將{}插入佇列".format (q.enqueue("A")))
print("已成功將{}插入佇列".format (q.enqueue("B")))
print("已成功將{}插入佇列".format (q.enqueue("C")))
print(q.size())