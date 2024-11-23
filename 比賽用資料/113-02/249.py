up = {'A':800, 'E':500, 'C':200}
down = {'A':800, 'E':400, 'C':100}

u, d = input().split(',')
u = u.rstrip(' ')
d = d.lstrip(' ')
people = len(u) + len(d)
m = 0
for i in u:
    m += up[i]
for i in d:
    m += down[i]
if people >= 20:
    print(int(m * 0.9))
else:
    print(m)