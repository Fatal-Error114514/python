x = input()
while(x != '0'):
    n,lst = x.split()
    n = len(lst) // int(n)
    lst = [lst[i:i+n][::-1] for i in range(0, len(lst), n)]
    print(*lst, sep='')
    x = input()
