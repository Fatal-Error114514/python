from sys import stdin

def Input():
    return stdin.readline().rstrip()

def height(p, n):    
    if(p > n) or (data[p] == None):             
        return 0
    else:
        Lcount= height(p*2,n)     
        Rcount= height(p*2+1,n)   
        return max(Lcount, Rcount) +1

for _ in range(int(Input())):
    data = [None] + eval(Input().replace('null', 'None'))
    n = len(data)-1
    root = 2
    ans = 0
    for i in range(3):
        left = height(root,n) 
        root += 1
        right = height(root,n) 
        ans = max(ans, left + right) 
    print(ans)   

