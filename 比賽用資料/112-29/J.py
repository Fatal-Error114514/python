for i in range(int(input())):
    n=int(input())
    if n%2!=0:
        print("7"+"1"*(n//2-1))
    else:
        print("1"*(n//2))