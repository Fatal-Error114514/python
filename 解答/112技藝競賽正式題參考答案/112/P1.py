s = input()
n, visited = len(s), set()
left, right = 0, 0
ans = (0, 0)
while right < n:
    if s[right] in visited and right - left > ans[1] - ans[0]:
        ans = (left, right)

    while s[right] in visited:
        visited.remove(s[left])
        left += 1
    visited.add(s[right])

    right += 1

if right - left > ans[1] - ans[0]:
    ans = (left, right)

print(ans[1] - ans[0])

