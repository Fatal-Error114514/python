from sys import stdin

def Input():
    return stdin.readline().rstrip()

while True:
    a = list(Input())
    b = list(Input())
    if(a == b == []):
        break
    same = set(a) & set(b)
    output = []
    for i in same:
        output.append(i *(min(a.count(i), b.count(i))))
    print(*sorted(output), sep='')

