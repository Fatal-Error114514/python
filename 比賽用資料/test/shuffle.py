n,m=map(int,input().split())
s=tuple(map(int,input().split()))
k=n//2
for _ in range(m):
    s=sum(zip(s[:k],s[k:]),())
print(*s)