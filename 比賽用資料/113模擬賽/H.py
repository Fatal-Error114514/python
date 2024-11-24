rom = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
m = list(input().split())
m = m[-1].rstrip('"').lstrip('"')
prev = 0
ans = 0
for i in reversed(m):
    curr = rom[i]
    if curr >= prev:
        ans += curr
    else:
        ans -= curr
    prev = curr
print(ans)