for _ in range(int(input())):
    num = sorted(list(map(int,input().split())), reverse = True)
    print(num[0], num[1])