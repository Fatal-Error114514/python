s = input()
stack = []
max_count = 0
invaild = -1
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        if stack:
            stack.pop()
            if stack:
                max_count = max(max_count, i - stack[-1])
            else:
                max_count = max(max_count, i - invaild)
        else:
            invaild = i
print(max_count)