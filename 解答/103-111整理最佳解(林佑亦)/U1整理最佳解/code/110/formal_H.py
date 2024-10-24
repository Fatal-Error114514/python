from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    temp = Input().split()
    lst = []
    for i in range(0, len(temp), 2):
        lst.append(int( (temp[i] + temp[i+1]), 16))
    lst = hex(sum(lst))[2:]
    while(len(lst) > 4):
        lst = hex(int(lst[:-4], 16) + int(lst[-4:], 16))[2:]
    lst = hex(int(lst, 16) ^ 65535)[2:]
    print(lst.zfill(4))

