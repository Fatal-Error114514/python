from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    print(int(int(Input())//int(Input())))
