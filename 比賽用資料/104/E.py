for _ in range(int(input())):
    n = bin(int(input()))[2:]
    print(sum(int(i) for i in n))