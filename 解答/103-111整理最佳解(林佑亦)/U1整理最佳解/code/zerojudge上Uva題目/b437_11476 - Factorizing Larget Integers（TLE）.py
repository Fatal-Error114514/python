# https://zerojudge.tw/ShowProblem?problemid=b437

for _ in range(int(input())):
    n = int(input())
    print(n,'= ',end='')
    output = []
    for i in range(2, int(n**0.5)+1):
        if(n % i == 0):
            break
    else:
        print(n)
        continue
    for i in range(2, n+1):
        for j in range(2, int(i**0.5)+1):
            if(i % j == 0):
                break
        else:
            count = 0
            while(n % i == 0):
                n //= i
                count += 1
            if(count > 1):
                output.append(str(i) + '^' + str(count))
            elif(count):
                output.append(str(i))
        if(n == 1):
            print(*output,sep=' * ')
            break
    else:
        print(n)

