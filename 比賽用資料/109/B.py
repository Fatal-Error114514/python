for _ in range(int(input())):
    A = []
    B = []
    for i in input():
        if i == '4':
            A.append('3')
            B.append('1')
        else:
            A.append(i)
            B.append('0')
    
    a = ''.join(A)
    b = ''.join(B)
    print(a, int(b))