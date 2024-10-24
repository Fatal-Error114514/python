c,shuffle=map(int,input().split())
card=list(map(int,input().split()))

for i in range(shuffle):
    n=c//2
    card=sum(zip(card[:n],card[n:]),())
print(*card)
