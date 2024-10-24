def greedy(n):
    """課程的貪婪演算法"""
    length=len(n)                                       #課程數量
    nlist=[]                                            #儲存結果
    nlist.append(n[0])                                  #第一節課
    n_endtime=nlist[0][1][1]                            #第一節課下課時間
    for i in range(1,length):                           #貪婪選課
        if n[i][1][0] >= n_endtime:                     #上課時間晚於或等於
            nlist.append(n[i])                          #加入貪婪選課
            n_endtime=n[i][1][1]                        #新的下課時間
    return nlist

n = {"化學":(12, 13),                                   #定義課程時間
     "英文":(9, 11),
     "數學":(8, 10),
     "計概":(10, 12),
     "物理":(11, 13),
    }

cs = sorted(n.items(), key=lambda item:(item[1][1],item[1][0]))      #課程時間排序
print("所有課程依下課時間排序如下")
print("課程","  開始時間 "," 下課時間")
for i in range(len(cs)):
    print(f"{cs[i][0]}{cs[i][1][0]:7d}:00{cs[i][1][1]:8d}:00")

s=greedy(cs)                                            #呼叫貪婪選課
print("貪婪排課時間如下")
print("課程","  開始時間 "," 下課時間")
for i in range(len(s)):
    print(f"{s[i][0]}{s[i][1][0]:7d}:00{s[i][1][1]:8d}:00")