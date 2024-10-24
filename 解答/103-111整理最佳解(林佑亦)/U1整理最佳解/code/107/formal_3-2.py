from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    s1,m1,s2,m2,s3,m3 = map(int,Input().split())
    count = 0
    for i in range(s1, m1+1):
        for j in range(s2, m2+1):
            for k in range(s3, m3+1):
                if((i+j) % k == (i-j) %k):
                    count += 1
    print(count)

