n = int(input())
c = list(map(int,input().split()))
a = 0
for i in range(n):
     for j in range(i):
        if c[j] > c[i]:
            a += 1
print(a)
