from sys import stdin

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    n = Input()[::-1]
    A = 0
    B = 0
    for i in range(len(n)):
        if(n[i] == '4'):
            A += 3 *(10**(i))
            B += 1 *(10**(i))
        else:
            A += int(n[i])*(10**(i))
    print(A,B)
