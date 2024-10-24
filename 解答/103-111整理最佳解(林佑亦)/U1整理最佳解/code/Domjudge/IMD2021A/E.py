n = int(input())
while n:
    n = bin(n)[2:]
    c = n.count('1')
    print(f'The parity of {n} is {c} (mod 2).')
    n = int(input())