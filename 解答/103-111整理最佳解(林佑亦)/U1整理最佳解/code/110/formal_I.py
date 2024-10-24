from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = Input()
    if(len(n) == 5):
        print(3)
    elif(len(set(n) & set('one')) >= 2):
        print(1)
    else:
        print(2)
