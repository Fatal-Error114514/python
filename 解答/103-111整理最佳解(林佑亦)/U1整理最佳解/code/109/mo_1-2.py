from sys import stdin

def Input():
    return stdin.readline().rstrip()

dic = [
    ['M', 1000],
    ['CM', 900],
    ['D', 500],
    ['CD', 400],
    ['C', 100],
    ['XC', 90],
    ['L', 50],
    ['XL', 40],
    ['X', 10],
    ['IX', 9],
    ['V', 5],
    ['IV', 4],
    ['I', 1]]

for _ in range(int(Input())):
    n = int(Input())
    output = ''
    for i in dic:
        a,n = divmod(n, i[1])
        if(a):
            output += i[0]*a
    print(output)

