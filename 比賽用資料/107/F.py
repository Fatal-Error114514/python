# (a + b) % m == (a - b) % m

for _ in range(int(input())):
    s1, m1, s2, m2, s3, m3 = map(int, input().split())
    count = 0
    for i in range(s1, m1 + 1):
        for j in range(s2, m2 + 1):
            for k in range(s3, m3 + 1):
                if (i + j) % k == (i - j) % k:
                    count += 1
    print(count)