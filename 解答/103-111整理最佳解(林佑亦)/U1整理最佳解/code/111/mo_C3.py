from sys import stdin

def Input():
    return stdin.readline().rstrip()
    
a,b = Input().split()
while(not a == b == '0'):
    a = list(a.zfill(max(len(a), len(b)))) # 補0補成一樣的位數，方便運算
    b = list(b.zfill(len(a))) # 因為a已經補成比較長的數字了，所以直接用len(a)
    plus = 0
    count = 0
    for i in range(len(a)): #其實也可以用for(len(a)-1, -1, -1) 這樣上面就不用把a、b轉成list了
        x = int(a.pop())
        y = int(b.pop())
        plus = (plus + x + y) // 10 #plus是進位的部分
        if(plus):
            count += 1
    if(count == 0):
        print('No carry operation.')
    elif(count == 1):
        print('1 carry operation.')
    else:
        print(f'{count} carry operations.')
    a,b = Input().split()
    