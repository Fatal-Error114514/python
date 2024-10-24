from itertools import permutations

for i in range(int(input())):
    l=int(input())
    arry=list(map(int,input().split()))
    target=arry[-1]
    arry=arry[0:l]
    for i in permutations(arry,2):
        if sum(i)==target:
            print("YES")
            break
    else:
        print("NO")