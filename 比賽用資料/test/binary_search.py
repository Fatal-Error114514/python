def search(lst):
    print(lst)
    low=0
    high=len(lst)-1
    mid=int((high+low)/2)
    times=0
    while True:
        times+=1
        if key==lst[mid]:   #找到了
            rtn=mid
            break
        elif key>lst[mid]:
            low=mid+1   #下一次往右搜尋
        else:
            high=mid-1  #下一次往左搜尋
        mid=int((high+low)/2)   #更新中間引索值
        if low>high:    #所有元素比較結束
            rtn=-1
            break
    return rtn,times
lst=[10,2,5,6,1,3,55,4]
lst=sorted(lst)
key=int(input("輸入搜索值："))
rtn,times=search(lst)
if rtn !=-1:
    print(f"在引索值{rtn}找到了，共找了{times}次")
else:
    print("查無此搜尋號碼")