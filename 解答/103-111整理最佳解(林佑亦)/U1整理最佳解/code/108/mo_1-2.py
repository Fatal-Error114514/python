from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    h1,m1,h2,m2 = map(int, Input().split())
    t1 = h1*60 + m1
    t2 = h2*60 + m2
    sleep = t2 - t1
    if(sleep < 0):
        sleep += 60*24
    print(sleep)
