from sys import stdin

def Input():
    return stdin.readline().rstrip()

dic = {
    1000:'M',
    900:'CM',
    500:'D',
    400:'CD',
    100:'C',
    90:'XC',
    50:'L',
    40:'XL',
    10:'X',
    9:'IX',
    5:'V',
    4:'IV',
    1:'I'
}

for _ in range(int(Input())):
    n = int(Input())
    output = ''
    for num,word in dic.items():
        a,n = divmod(n, num)
        output += word * a
    print(output)