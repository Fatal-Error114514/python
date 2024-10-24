n = input()
while n:
    lst = sorted(list(map(int,n.split(','))))
    print(*lst)
    n = input()