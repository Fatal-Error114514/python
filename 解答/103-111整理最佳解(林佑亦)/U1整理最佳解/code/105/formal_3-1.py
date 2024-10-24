from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = [''] + list(map(int,Input().split(',')))
    lflag = None
    rflag = None
    for i in range(1, len(lst)):
        if(i*2 < len(lst)):
            if(lflag == None):
                lflag = lst[i] < lst[i*2]
            elif(lflag != (lst[i] < lst[i*2])):
                print('F')
                break
        if(i*2 +1 < len(lst)):
            if(rflag == None):
                rflag = lst[i] < lst[i*2+1]
            elif(rflag != (lst[i] < lst[i*2+1])):
                print('F')
                break
    else:
        if(lflag == rflag):
            print('H')
        else:
            print('B')
