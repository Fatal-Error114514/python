from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = Input().split()
    p = 0
    while(len(lst) > 1):
        while(lst[p][-1].isdigit()): #[-1]因為0.5.isdigit()會回傳False所以都抓最右邊的字來判斷
            p += 1
        lst[p] = str(int(eval(lst[p-2] + lst[p] + lst[p-1])))
        del lst[p-1]
        del lst[p-2]
        p -= 2
    print(lst[0])

