f=[]
n=int(input())
for i in range(2,n):
    while n%i==0:
        f.append(i)
        n//=i
if n!=1:
    f.append(n)
print(*f)