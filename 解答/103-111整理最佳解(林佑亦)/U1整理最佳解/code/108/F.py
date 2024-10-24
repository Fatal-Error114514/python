from sys import stdin

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    a,b = map(int,Input().split())
    q = []
    count = 0
    ans = ''
    while(count <= 50):
        s,a = divmod(a, b)
        ans += str(s)
        if(a == 0):
            print(ans[0] + '.' + ans[1:] + '(0)')
            break
        elif(a in q):
            p = q.index(a) +1
            print(ans[0] + '.' + ans[1:p] + '(' + ans[p:] + ')')
            break
        q.append(a)
        a *= 10
        count += 1
    else:
        print(ans[0] + '.(' + ans[1:] + '...)')