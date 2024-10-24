s=[]

for _ in range(int(input())):
    
    s.append(int(input()))
    s.sort()

    if len(s)%2!=0:
        print(s[len(s)//2])
    else:
        print((s[len(s)//2] + s[len(s)//2-1]) // 2)