from itertools import combinations

def check(lst):
    for j in combinations(lst, len(lst)//2):
        if sum(j) == sum(lst) - sum(j):
            return 1
    return 0
lst = list(map(int,input().split(',')))
print(check(lst))