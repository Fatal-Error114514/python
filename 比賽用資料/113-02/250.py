s = list('ABCDEF')
num = list(map(int,input().replace('{', '').replace('}', '')))
while num:
    i = num.pop(0)
    s.insert(i, s[0])
    s.pop(0)
print(''.join(s))