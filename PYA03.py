n = input()
limit = 0
t = True
for i in n[:5]:
    if int(i) % 2 != 0:
        if limit < 2:
            limit += 1
        else:
            t = False
s = (int(n[0]) + int(n[2]) + int(n[4]) + (int(n[1]) + int(n[3])) * 5) % 28
if s > 65:
    s = chr(s)
else:
    s = chr(s + (65 - s - 1))
if t and s == n[5]:
    print('Pass')
else:
    print('Fail')