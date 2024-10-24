from sys import stdin

def Input():
    return stdin.readline().rstrip()

a = int(Input())
b = int(Input())
for i in range(min(a, b)+1, max(a, b)):
    if(i % 5 == 2) or (i % 5 == 3):
        print(i)

