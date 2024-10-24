from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = int(Input())
lst = list(map(int,Input().split()))
ans = sum(lst)
if(ans % 2 == 0):
    print(ans)
else:
    for i in sorted(lst):
        if(i % 2 != 0):
            ans -= i
            break
    print(ans)
