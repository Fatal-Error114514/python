from collections import deque

graph={}
graph["Tom"]=["Ivan","Ira","kevin"]
people=deque()
people+=graph["Tom"]
print("列出people資料類型:",type(people))
print("列出搜尋名單      :",people)
for i in range(len(people)):
    print(people.popleft())

people.append("Ivan")
people.append("Ira")
print("列出名單:",people)
people.appendleft("Unistar")
print("列出名單:",people)
people.appendleft("Ice Rain")
print("列出名單:",people)