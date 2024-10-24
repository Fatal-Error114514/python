from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b = map(eval,Input().replace('}, {', '}; {').split(';'))
    lst = [a|b, a&b, a-b, a^b]
    output = []
    for i in lst:
        if(i):
            output.append(str(sorted(list(i))).replace('[', '{').replace(']', '}'))
        else:
            output.append('N')
    print(*output,sep=', ')
