from sys import stdin

def Input():
    return stdin.readline().rstrip()

l = Input()
while l:
    n = int(l)
    total = 0
    for i in range(2, n//2+1): # 從我到我的一半開始找，因為最多只會到一半 ex: 10 => 5 + 5
        for j in range(2, int(i**0.5)+1): # 用j來判斷i是不是質數
            if(i % j == 0): # 是的話就break
                break # break不是正常離開迴圈，所以不會進入else
        else:
            x = n - i # x是i的補數，n = x+i
            for j in range(2, int(x**0.5)+1): # 用j來判斷x是不是質數
                if(x % j == 0): # 是的話就break
                    break # break不是正常離開迴圈，所以不會進入else
            else:
                total += 1
    print(total)
    l = Input()


