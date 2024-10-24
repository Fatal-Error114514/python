from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(Input())
    for i in range(n//2, n):
        if(i + sum(list(map(int,str(i)))) == n):
            print(i)
            break
    else:
        print(0)
