from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = ''
    for i in range(1, int(Input())+1):
        lst += str(i)

    output = []
    for i in range(10):
        output.append(lst.count(str(i)))

    print(*output)

