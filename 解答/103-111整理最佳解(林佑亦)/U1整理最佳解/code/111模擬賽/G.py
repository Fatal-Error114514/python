from sys import stdin
from decimal import Decimal

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b = Input().split()
    print(Decimal(a) * Decimal(b))

#如果不用涵式要這樣寫
# for _ in range(int(Input())):
#     a,b = Input().split()
#     dot = 0
#     if('.' in a):
#         dot += len(a) - a.find('.')-1
#         a = a.replace('.', '')
#     if('.' in b):
#         dot += len(b) - b.find('.')-1
#         b = b.replace('.', '')
#     a = int(a)
#     b = int(b)
#     ans = str(a*b)
#     dot = len(ans) - dot
#     ans = ans[:dot] + '.' + ans[dot:]
#     print(ans)


