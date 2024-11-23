lst = list(map(int,input().split(', ')))
count = 0
for i in lst:
    for j in lst:
        if j == i:
            continue
        if j%i != 0:
            break
    else:
        count += 1
print(count)