from sys import stdin

def Input():
    return stdin.readline().rstrip()

dic = {}
for _ in range(int(Input())):
    country,*name = Input().split()
    if(country not in dic): dic[country] = 0 #字典沒這個國家，就把他設為0
    dic[country] += 1
dic = sorted(dic.items())
for i in dic:
    print(*i)
