s = list(input())
count = 0
output = []
i = 0
while len(s) > i:
    count = 0
    curr = s[i]
    while len(s) > i and s[i] == curr:
        i += 1
        count += 1
    output.append(str(curr) + str(count))
print(*output, sep = '')