from sys import stdin

def Input():
    return stdin.readline().strip()

def Stairs(n):
    m = n//2
    dot = '*'
    line = '*' *(n+1)
    for i in range(n - m):
        for j in range(n):
            print(dot)
        if(i != m):
            print(line)
        line = ' '*n + line
        dot = ' '*n + dot

n = int(Input())
Stairs(n)
