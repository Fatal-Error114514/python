from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    lst = Input().replace('x','*x')
    lst = lst.replace('=', '-(') + ')'
    lst = lst.replace('(*', '(')
    lst = lst.replace('+*', '+')
    lst = lst.replace('-*', '-')
    lst = lst.lstrip('*')
    lst = eval(lst, {'x': 1j})
    x = lst.imag *-1
    n = lst.real
    if(x == n == 0):
        print('IS')
    elif(x == 0):
        print('NS')
    else:
        print(int(n/x))


