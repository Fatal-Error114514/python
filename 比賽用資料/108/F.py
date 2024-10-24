for _ in range(int(input())):
    a, b = map(int, input().split())

    q, r = divmod(a, b)
    qs = []
    rs = []
    while r not in rs:
        qs.append(q)
        rs.append(r)
        q, r = divmod(r * 10, b)
    qs.append(q)
    rs.append(r)

    i = rs.index(rs[-1])
    nonrepeating_part = qs[1:i + 1]
    repeating_part = qs[i + 1:]
    if len(repeating_part) > 50:
        repeating_part = [*repeating_part[:50], '...']

    print(qs[0], '.', *nonrepeating_part, '(', *repeating_part, ')', sep='')