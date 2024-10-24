from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    m,k = map(int,Input().split(','))
    print(len(str(pow(m,k))))
