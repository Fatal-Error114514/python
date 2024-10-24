from sys import stdin

def Input():
    return stdin.readline().rstrip()

lst = eval(Input())
print(str(list(map(list,zip(*lst[::-1])))).replace(' ',''))


