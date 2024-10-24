# https://zerojudge.tw/ShowProblem?problemid=c013
n = int(input())
A = input()
for i in range(n):
    p = 1
    A = int(input())
    size = A*2-1
    output = ['']*size
    F = int(input())
    for j in range(1,A+1):
        output[p-1] = str(j)*p
        if(size - p != p - 1):
            output[size - p] = str(j)*p 
        p += 1
    for j in range(F):
        print(*output,sep= '\n')
        if(j < F):
            print()