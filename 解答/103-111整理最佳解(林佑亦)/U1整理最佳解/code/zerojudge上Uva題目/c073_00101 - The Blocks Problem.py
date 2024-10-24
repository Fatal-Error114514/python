# c073: 00101 - The Blocks Problem
LST = []
locate = []
do = ''
a = 0
act = ''
b = 0

def CUT(n):
    try:
        global do,a,act,b
        r = 0
        do,a,act,b = n.split()
        a = int(a)
        b = int(b)
    except:
        r = -1
    return r

def NUM(X):
    return LST[locate[X]].index(X)

def GOBACK(X):
    for i in range(NUM(X)+1,len(LST[locate[X]])):
        LST[LST[locate[X]][i]].append(LST[locate[X]][i])        #LST[locate(X)][i] => 該數字
        del LST[locate[X]][i]

def MOVE_ONTO(A,B):
    GOBACK(A)
    GOBACK(B)
    LST[locate[B]].append(A)
    del LST[locate[A]][NUM(A)]
    locate[A] = locate[B]

def MOVE_OVER(A,B):
    GOBACK(A)
    LST[locate[B]].append(A)
    del LST[locate[A]][NUM(A)]
    locate[A] = locate[B]

def PILE_ONTO(A,B):
    GOBACK(B)
    l = locate[A]
    n = NUM(A)
    for i in range(n,len(LST[l])):
        LST[locate[B]].append(LST[locate[A]][n])
        locate[LST[locate[A]][n]] = locate[B]
        del LST[locate[A]][n]
    
def PILE_OVER(A,B):
    l = locate[A]
    n = NUM(A)
    for i in range(n,len(LST[l])):
        LST[locate[B]].append(LST[l][n])
        locate[LST[l][n]] = locate[B]
        del LST[l][n]


def BORN_LIST(n):                    #產生陣列
    for i in range(int(n)):
        LST.append([i])
        locate.append(i)

def OUTPUT():                        #輸出
    for i in range(len(LST)):
        print(i,": ",end='',sep = '')
        print(*LST[i])
            
while True:
    try:
        n = input("")
        if(n[:4] == 'quit'):
            OUTPUT()
            continue
        elif(n.isdigit()):
            LST = []
            locate = []
            BORN_LIST(n)
        else:
            if(CUT(n) == -1):
                continue
            if(locate[a] != locate[b]):
                if(do == 'move' and act == 'onto'):
                    MOVE_ONTO(a,b)
                elif(do == 'move' and act == 'over'):
                    MOVE_OVER(a,b) 
                elif(do == 'pile' and act == 'onto'):
                    PILE_ONTO(a,b)
                elif(do == 'pile' and act == 'over'):
                    PILE_OVER(a,b)
    except EOFError:
        break