from sys import stdin
n = int(stdin.readline())
def fun(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
for h in range(n):
    a,b = map(int,stdin.readline().split(","))
    if b-a != 2:
        print("N")
    elif fun(a) and fun(b):
        print("Y")
    else:
        print("N")