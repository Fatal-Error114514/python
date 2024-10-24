from sys import stdin

def Input():
    return stdin.readline().rstrip()

lst = []
for _ in range(9):
    lst.append(Input())

if(lst.count('Tiger') > 4):
    print('Tiger')
else:
    print('Lion')
