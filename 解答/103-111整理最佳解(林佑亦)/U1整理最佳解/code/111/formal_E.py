n = input()
lst = list(map(int,input().split()))
dic = {}
for i in set(lst):
    dic[i] = lst.count(i)
    for j in range(dic[i]):
        lst.remove(i)
lst = sorted(list(dic.items()))
for i in lst:
    print(*i)