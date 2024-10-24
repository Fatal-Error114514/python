from sys import stdin

def Input():
    return stdin.readline().rstrip()

n = int(Input())
lst = list(map(int,Input().split()))
total = 0
for i in range(1, len(lst)):
    for j in range(i):
        if(lst[j] > lst[i]):
            total += 1
print(total)




