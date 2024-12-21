s = list(input())
for i in range(len(s)):
    if int(s[i]):
        s[i] = '0'
    else:
        s[i] = '1'
print(''.join(s))