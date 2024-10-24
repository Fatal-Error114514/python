n = input()
dic = {}
for i in set(n):
    dic[ord(i)] = n.count(i)
lst = list(dic.items())
lst.sort(key= lambda x:(x[1], -x[0]))
for i in lst:
    print(*i)

