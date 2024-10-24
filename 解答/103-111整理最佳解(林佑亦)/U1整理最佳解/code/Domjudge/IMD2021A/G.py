lst = []
for _ in range(int(input())):
    g,s,b,*contry = input().split()
    lst.append([int(g), int(s), int(b), contry])
lst.sort(reverse= True)
print(*lst[0][3])









