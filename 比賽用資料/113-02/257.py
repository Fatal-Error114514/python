s = input()
balance = 0
max_depth = 0
for i in s:
    if i == '{':
        balance += 1
        max_depth = max(max_depth, balance)
    elif i == '}':
        balance -= 1
        if balance < 0:
            print(-1)
            break
else:
    if balance != 0:
        print(-1)
    else:
        print(max_depth)