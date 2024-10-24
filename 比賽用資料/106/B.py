for _ in range(int(input())):
    rom = {
        'I':1, 'V':5, 'X':10,
        'L':50, 'C':100, 'D':500, 
        'M':1000
        }
    s = input()
    num = 0
    prev = 0
    for i in reversed(s):
        current = rom[i]
        if current >= prev:
            num += current
        else:
            num -= current
        prev = current
    print(num)