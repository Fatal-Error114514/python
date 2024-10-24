m=[list(map(int,input().split()))for _ in range(3)]

a,b,c=map(sum,m)

s=(a+b+c)//2

a,b,c=s-a,s-b,s-c

m[0][0]=a
m[1][1]=b
m[2][2]=c

for row in m:
    print(*row)