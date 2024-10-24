from sys import stdin

def Input():
    return stdin.readline().strip()

lst = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I']
]

for _ in range(int(Input())):
    n = Input()
    output = 0
    for i in lst:
        while(n.find(i[1]) == 0):
            output += i[0]
            n = n.replace(i[1], '', 1)
    print(output)
