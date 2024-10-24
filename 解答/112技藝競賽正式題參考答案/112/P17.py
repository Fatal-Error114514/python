s = input()
xss = [s[:3], s[3:6], s[6:]]
xss_prime = list(zip(*xss))  # 行列互換

def f(rows):
    for row in rows:
        if len(set(row)) == 1:
            return 1 if row[0] == 'O' else 2
    return 3

def g(rows):
    if len(set([rows[0][0], rows[1][1], rows[2][2]])) == 1:
        return 1 if rows[0][0] == 'O' else 2
    return 3

print(min(f(xss), g(xss), f(xss_prime), g(xss_prime)))
