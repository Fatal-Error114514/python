from sys import stdin

def Input():
    return stdin.readline().rstrip()

a = list(map(int,Input().split()))
b = list(map(int,Input().split()))
total = 0
for i in range(3):
    total += a[i] * b[i]
print(total)
