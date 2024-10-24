n=int(input())
a=0
while True:
    if 2**a>n:
        a-=1
        break
    a+=1
print(2**a)