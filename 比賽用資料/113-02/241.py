n = input()
ans = 0
for i in range(len(n)):
    for j in range(i, len(n)):
        if n[i] == n[j] and len(n[i:j + 1]) > 3 and n[i].isupper() and n[j].isupper():
            ans += 1
print(ans)