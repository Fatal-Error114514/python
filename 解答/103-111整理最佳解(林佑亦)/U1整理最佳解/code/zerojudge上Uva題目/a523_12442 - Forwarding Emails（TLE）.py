#https://zerojudge.tw/ShowProblem?problemid=a523
from sys import stdin

def Input():
    return stdin.readline().rstrip()

for x in range(int(Input())):
    n = int(stdin.readline().strip())  
    to = [0]*(n+1)                    
    ans = [0]*(n+1)
    for h in range(n):
        a,b = map(int,stdin.readline().split()) 
        to[a] = b      
    for i in range(1,n+1):   
        p = i                   
        check = [0]*(n+1)    
        while check[p] != 1:    
            check[p] = 1        
            p = to[p]            
        ans[i] = sum(check)  
    print(f'Case {x+1}: {ans.index(max(ans))}')    
