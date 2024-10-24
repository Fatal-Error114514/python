# https://zerojudge.tw/ShowProblem?problemid=c067
num = 1
while True:
    move = 0
    n = int(input())
    if(n == 0):
        break
    blocks = input().split()
    for i in range(n):
        blocks[i] = int(blocks[i])
    balance = sum(blocks) // n
    while max(blocks) != balance:
        blocks.sort()
        blocks[0] += 1
        blocks[n-1] -= 1
        move += 1
    print('Set #',num,sep='')
    print('The minimum number of moves is ',move,'.',sep='')
    num += 1