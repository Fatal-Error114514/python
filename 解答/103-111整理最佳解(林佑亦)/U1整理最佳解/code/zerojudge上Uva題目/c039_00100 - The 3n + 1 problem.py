# https://zerojudge.tw/ShowProblem?problemid=c039
def COUNT(n):                  #數
    count = 1
    while True:
        if(n == 1):
            return count
        elif(n % 2 != 0):
            n = 3*n + 1
        else:
            n = n / 2
        count += 1

while True:
    try:
        A,B = map(int,input("").split())
        if(A > B):
            max = 0
            for i in range(B,A+1):
                if(COUNT(i) > max):
                    max = COUNT(i)
            print(A,B,max)
        else:
            max = 0
            for i in range(A,B+1):
                if(COUNT(i) > max):
                    max = COUNT(i)
            print(A,B,max)
    except EOFError:
        break