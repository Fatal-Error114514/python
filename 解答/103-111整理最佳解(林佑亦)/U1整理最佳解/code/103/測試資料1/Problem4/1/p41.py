from sys import stdin
n = int(stdin.readline())
def check(x):
    global ans
    global a
    for i in asc:
        if x[0:len(i)] == i:
            ans += str(asc.index(i))
            a = x[len(i):]
            break
for h in range(n):
    a = stdin.readline()
    asc = ["00","01","100","101","1100","1101","11100","11101","111100","111101"]
    ans = ""
    for j in range(2):
        check(a)
    ans = int(ans)+3
    if ans>26:
        ans-=26
    print(chr(ans+64))



