def prime(n):
    x = n
    i = 2
    ans = ""

    while n > 1:

        while n % i == 0:     #只要n除以i可以整除，則除到不能整除為止
            n //= i
            if n>1:
              ans+= str(i) + " x "
            else:
              ans+= str(i)
        i+=1

    print(x,"=",ans)

while True:
    n=int(input())
    if n==-9999:
       break
    else:
       prime(n)