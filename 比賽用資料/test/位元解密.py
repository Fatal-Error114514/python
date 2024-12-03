# 題目: 給一個加密的lst，lst[i] = lst[1] ^ lst[2] ... ^ lst[i]

lst = list(map(int,input().split(',')))
for i in range(1, len(lst)):
    lst[i] = lst[i - 1] ^ lst[i]
print(*lst, sep =',')