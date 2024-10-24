# https://zerojudge.tw/ShowProblem?problemid=a521
k = input()
while k:
    x = list(map(ord, list(k)))
    flag = False
    for i in range(1, 10001):
        lst = list(map(lambda x:x+(i-65), x))
        lst = ''.join(map(str, lst))
        while(len(lst) > 2):
            if(lst == [1, 0, 0]):
                print(i)
                flag = True 
                break
            temp = []
            for j in range(len(lst)-1):
                temp.append((int(lst[j]) + int(lst[j+1])) %10)
            lst = temp
        if(flag):
            break
    else:
        print(':(')
    
    k = input()



