n=[list(map(int,input().split()))for i in range(3)]

a,b,c=n[0][0],n[1][1],n[2][2]

s=(sum(n[0])+sum(n[1])+sum(n[2]))//2

a,b,c=s-sum(n[0]),s-sum(n[1]),s-sum(n[2])

n[0][0]=a
n[1][1]=b
n[2][2]=c

for i in n:
    print(*i)