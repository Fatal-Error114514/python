from sys import stdin


groups = ' '.join(line.strip() for line in stdin.readlines())
for group in groups[:-3].split(' () '):
    xrs = sorted((s[1:-1].split(',') for s in group.split()), key=lambda xr: xr[1])
    illegal = xrs[0][1] != ''
    s = set([''])
    if not illegal:
        for _, r in xrs[1:]:
            if r in s or r[:-1] not in s:
                illegal = True
                break
            s.add(r)
    if illegal:
        print('not complete')
        continue

    print(*(x for x, _ in sorted(xrs, key=lambda xr: (len(xr[1]), xr[1]))))
