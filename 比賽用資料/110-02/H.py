for _ in range(int(input())):
    n = input().split()
    lst = []
    for i in range(0, len(n), 2):
        lst.append(int(n[i] + n[i + 1], 16))
    lst = hex(sum(lst))[2:]
    if len(lst) > 4:
        lst = hex(int(lst[:1], 16) + int(lst[1:], 16))
        lst = hex(int(lst, 16) ^ 0xffff)[2:]
    print(f'{lst:0>4}')