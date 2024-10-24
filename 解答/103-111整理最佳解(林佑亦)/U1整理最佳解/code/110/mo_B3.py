from sys import stdin

def Input():
    return stdin.readline().rstrip()

for i in range(int(Input())):
    n = int(Input())
    print(f'Case {i+1}: ',end='')
    if(n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        print('a leap year')
    else:
        print('a normal year')
