from collections import Counter

def max_index(lst):
    max_n = max(lst.values())
    index = []
    for i in lst.keys():
        if lst[i] == max_n:
            index.append(i)

    return sorted(index)


input()
lst = Counter(map(int,input().split()))
print(*max_index(lst))