from sys import stdin

def Input():
    return stdin.readline().strip()

M,N = map(int, Input().split(','))
if(M % 2 != 0):
    M += 1

for i in range(M, N+1, 2):  # M~N的數字
    count = 0
    for j in range(2, i//2+1):   # 尋找第一個數
        for k in range(2, int(j**0.5)+1):   # 確定是不是質數
            if(j % k == 0):
                break
        else:
            x = i - j # 找補數
            for k in range(2, int(x**0.5)+1):   # 質數判斷
                if(x % k == 0):
                    break
            else:
                if(x == j):
                    count += 1
                else:
                    count += 2
    if(count):
        print(i, count)
if(count):
    print('哥德巴赫猜想可能是對的')
else:
    print('哥德巴赫猜想是錯的')