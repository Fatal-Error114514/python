from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    num = 1
    for i in range(int(Input())-1):
        num = 2*(num +1)
    print(num)


"""
n = 4，an = 1

a4 = a3/2 -1 = 1
a3 = a2/2 -1 = 4
a2 = a1/2 -1 = 10
a1 = 22

a的n-1項 = 2*(an +1)
"""

