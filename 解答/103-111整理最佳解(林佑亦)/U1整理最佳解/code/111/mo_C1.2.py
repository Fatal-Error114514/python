from sys import stdin

def Input():
    return stdin.readline().rstrip()

#先把質數表建好
U = 2**15 +1
prime = [1] *U
prime[0] = prime[1] = False #0跟1不是質數，先寫好
for p in range(2, int(U**0.5)): #從二開始把自己的倍數變False
    if(prime[p]):
        s = 2 *p #從下一個p的倍數開始
        for i in range(s, U, p):
            prime[i] = 0 #把i變False

n = int(Input())
while n:
    counter = 0
    h = (n // 2) +1
    for i in range(2, h):
        if(prime[i] and prime[n-i]):
            counter += 1
    print(counter)
    n = int(Input())
