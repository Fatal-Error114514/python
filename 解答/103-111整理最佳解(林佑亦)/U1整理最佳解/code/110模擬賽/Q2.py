from sys import stdin

def Input():
    return stdin.readline().strip()

l1 = 'qwertyuiop'
l2 = 'asdfghjkl'
l3 = 'zxcvbnm'
def change(x):
    if(l1.count(x)):
        return l1[l1.index(x)-3]
    if(l2.count(x)):
        return l2[l2.index(x)-3]
    if(l3.count(x)):
        return l3[l3.index(x)-3]

n = input()
for i in n:
    if(i.isalpha()):
        if(i.islower()):
            i = change(i)
        else:
            i = change(i.lower()).upper()
    print(i, end='')
print()
