s=input()
n,visited=len(s),set()
left,right=0,0
ans=(0,0)
while right<n:
    if s[right] in visited and right-left>ans[1]-ans[0]:   #檢查目前窗口長度是否大於ans紀錄的長度
        ans=(left,right)
    
    while s[right] in visited:
        visited.remove(s[left])     #縮小窗口的左邊界，使窗口的字元不得重複
        left+=1
    
    visited.add(s[right])           #將right指向的字元加到visited集合中
    right+=1                        #right向右移動一位，檢查下一個字元

if right-left>ans[1]-ans[0]:        #重新檢查目前窗口長度是否大於ans紀錄的長度
    ans=(left,right)

print(ans[1]-ans[0])