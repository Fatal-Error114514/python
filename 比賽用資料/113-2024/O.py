s = input().split()
p = 0
while len(s) > 1:
    while s[p][-1].isdigit():
        p += 1
    c = s[p]
    b = s[p - 1]
    a = s[p - 2]
    s[p] = str(int(eval(a + c + b)))
    del s[p - 1]
    del s[p - 2]
    p -= 2
print(s[0])