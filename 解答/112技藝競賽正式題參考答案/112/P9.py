n1, n2 = int(input()), int(input())

ans = 0
for k in range(n1, n2 + 1):
    if all(t != 0 and k % t == 0 for t in map(int, str(k))):
        ans += 1

print(ans)
