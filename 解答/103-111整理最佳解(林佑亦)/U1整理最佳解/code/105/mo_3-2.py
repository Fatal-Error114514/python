from sys import stdin

def Input():
    return stdin.readline().rstrip()

lst = []
for i in range(int(Input())):
    lst.append(int(Input()))
print(*sorted(lst), sep=',')