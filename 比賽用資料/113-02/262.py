#a:97 A:65 z:122 Z:90
s = list(input())
move = int(input())
encode = []
for i in s:
    if i.isupper():
        if ord(i) + move > 90:
            encode.append(chr(ord(i) + move - 90 + 65 - 1))
        else:
            encode.append(chr(ord(i) + move))
    else:
        if ord(i) + move > 122:
            encode.append(chr(ord(i) + move - 122 + 97 - 1))
        else:
            encode.append(chr(ord(i) + move))
for i in range(len(s)):
    print(s[i], encode[i])
print(''.join(encode))