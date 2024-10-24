#https://zerojudge.tw/ShowProblem?problemid=a467
n = input()
while(n != '~'):
    ans = ''
    n = n.split()[:-1]
    flag = '0'
    for i in n:
        if(i == '0'):
            flag = '1'
        elif(i == '00'):
            flag = '0'
        else:
            ans += (len(i)-2) *flag
    print(int(ans, 2))
    n = input()
