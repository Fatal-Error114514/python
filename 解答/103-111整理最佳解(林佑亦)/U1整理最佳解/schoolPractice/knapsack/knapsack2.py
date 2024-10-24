#一維的
def knapsack(s):
    s = s.split()

    n = int(s[0])*2
    name = [i for i in s[1::3]]
    kg = [int(float(i)*2) for i in s[2::3]]
    exp = [int(i) for i in s[3::3]]
    
    lst = [0]*(n+1)
    namelst = ['']*(n+1)
    for i in range(len(kg)):
        for j in range(n, kg[i]-1, -1):
            if(lst[j] < exp[i] + lst[j-kg[i]]):
                lst[j] = exp[i] + lst[j-kg[i]]
                namelst[j] = namelst[j-kg[i]] + name[i] + '+'
    print(lst[-1])
    print(namelst[-1][:len(namelst[-1])-1:])

knapsack("2 衛武營 0.5 7 駁二特區 0.5 6 西子灣 1 9 義大世界 2 9 大港橋 0.5 8")