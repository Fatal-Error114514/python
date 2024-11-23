s = input()
max_len = 0
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if len(set(s[i:j + 1])) >= 3 and s[i:j + 1] == s[i:j + 1][::-1]:
            max_len = max(len(s[i: j +1]), max_len)
print(max_len)