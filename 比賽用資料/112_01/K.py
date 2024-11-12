#10000席座位 每區100排，一三區 2500席，每排25人，二區5000席，每排50人
n = int(input())
if n <= 2500:
    a, b = divmod(n, 25)
    if b >= 1:
        print(1, a + 1, b)
    else: print(1, a, 25)
elif n <= 7500:
    a, b = divmod(n - 2500, 50)
    if b >= 1:
        print(2, a + 1, b)
    else: print(2, a, 50)
else:
    a, b = divmod(n - 7500, 25)
    if b >= 1:
        print(3, a + 1, b)
    else: print(3, a, 25)