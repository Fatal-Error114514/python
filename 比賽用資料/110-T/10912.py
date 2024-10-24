val = [
        1000, 900, 500, 400,
        100, 90, 50, 40, 10,
        9, 5, 4, 1
]

syb = [
    'M', 'CM', 'D', 'CD', 
    'C', 'XC', 'L', 'XL',
    'X', 'IX', 'V', 'IV',
    'I'
]
for _ in range(int(input())):
    n = int(input())
    roman = ''
    for i in range(len(val)):
        while n >= val[i]:
            roman += syb[i]
            n -= val[i]
    print(roman)