from sys import stdin

def Input():
    return stdin.readline().rstrip()

for g in range(int(Input())):
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
    print(ans.index(max(ans)))    
