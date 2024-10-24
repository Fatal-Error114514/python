from sys import stdin
n = int(stdin.readline().strip())
# python3 p1-1.py < in1.txt
for h in range(n):
    a,b = map(str,stdin.readline().strip().split(","))
    if a == b:
        print(0)
    elif a == "Y" and b == "P":
        print(1)
    elif a == "O" and b == "Y":
        print(1)
    elif a == "P" and b == "O":
        print(1)
    else:
        print(2)