from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = list(Input())
    ans = 0
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            temp = lst[i:j+1]
            if(temp == temp[::-1]):
                ans = max(ans, j-i+1)
    print(ans)



