from sys import stdin

def Input():
    return stdin.readline().strip()

lst = list(map(int,Input().split(',')))
flag = max(lst) // 2
for i in range(flag, 1, -1):
    for j in range(2, int(i**0.5)+1):
        if(i % j == 0):
            break
    else:
        x = i
        break
lst.sort(key= lambda y:y%x)
print(*lst,sep=',')


