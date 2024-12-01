s = input()
max_num = 0
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if int(s[i:j]) % 2 != 0 and int(s[i:j]) > max_num:
            max_num = int(s[i:j])
print(max_num)