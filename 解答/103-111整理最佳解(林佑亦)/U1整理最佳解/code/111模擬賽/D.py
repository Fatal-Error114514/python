from sys import stdin

def Input():
    return stdin.readline().rstrip()

memo = []
def tree(n):
    if memo[n]:
        return memo[n]
    cnt = 0
    for i in range(1, n+1):
        cnt += tree(i-1) * tree(n-i)
    memo[n] = cnt
    return memo[n]

#catalan
for _ in range(int(Input())):
    n = int(Input())
    memo = [0 for i in range(n + 1)]
    memo[0] = memo[1] = 1
    ans = 0
    if n < 2:
        ans = memo[n]
    elif n % 2 == 1:
        ans = tree((n - 1) // 2)
    print(ans)



