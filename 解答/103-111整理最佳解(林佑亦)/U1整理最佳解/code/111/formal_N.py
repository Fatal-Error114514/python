# 這就是個最常遞增子序列
n = int(input())
lst = list(map(int,input().split()))
table = [lst.pop(0)]
for i in lst:
    if(i > table[-1]):
        table.append(i)
    else:
        for idx,num in enumerate(table):
            if(num > i):
                table[idx] = i
                break
print(len(table))