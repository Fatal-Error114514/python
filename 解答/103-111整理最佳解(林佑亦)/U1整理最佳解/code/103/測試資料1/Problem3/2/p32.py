from sys import stdin
n = int(stdin.readline())
for h in range(n):
    a = int(stdin.readline())
    x = a
    f0 = 0
    f1 = 1
    f2 = 1
    f3 = 2
    lis = []
    while f0<a:
        f3 = f1+f2
        f0 = f1
        f1 = f2
        f2 = f3
        lis.append(f1)
    lis.reverse()
    ans = [0 for i in range(len(lis))]
    for i in range(len(lis)):
        if a - lis[i] >=0:
            a -= lis[i]
            ans[i] = 1
    while ans[0] == 0:
        ans.pop(0)
    print(x,"=",sep="",end="")
    print("".join(str(i) for i in ans))


