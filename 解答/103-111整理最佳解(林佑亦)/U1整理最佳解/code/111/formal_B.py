a,b = map(int,input().split())
n = b - a
if(n < 0):
    n += 200
print(n)