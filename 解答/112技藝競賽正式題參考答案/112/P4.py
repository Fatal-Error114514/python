x, y, z = 0, 0, 0

s = input()

for c in s:
    if c == '{':
        x += 1
    elif c == '}':
        x -= 1
    elif c == '[':
        y += 1
    elif c == ']':
        y -= 1
    elif c == '(':
        z += 1
    else:
        z -= 1

    if -1 in [x, y, z]:
        print(0)
        break
else:
    print(int(x == y == z == 0))


