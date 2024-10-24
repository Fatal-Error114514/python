from sys import stdin
n = int(stdin.readline().strip())
# python3 p21.py<in1.txt
for i in range(n):
    data = stdin.readline().strip()
    ans = 0
    r = 15
    for j in data:
        x = int(j)*(r%2+1)
        if x>9:
            x-=9
        ans += x
        r-=1
    if ans%10 == 0:
        print("T")
    else:
        print("F")


