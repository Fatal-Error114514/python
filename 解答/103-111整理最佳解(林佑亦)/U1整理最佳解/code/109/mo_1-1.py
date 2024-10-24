from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = int(Input())
    for i in range(n-1, 1, -1):
        for j in range(2, int(n**0.5)+1):
            if(i % j == 0):
                break
        else:
            print(i)
            break

