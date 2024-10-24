while True:
    n = input()
    if n[0] == '0': break
    g, s = map(str, n.split())
    g = len(s) // int(g)
    group = [s[i : i + g][::-1] for i in range(0, len(s), g)]

    r = ''.join(group)
    print(r)