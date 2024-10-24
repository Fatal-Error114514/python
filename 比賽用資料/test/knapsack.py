def greedy(n):
    """商品貪婪演算法"""
    length = len(n)                                           #商品數量
    n_list = []                                               #儲存結果
    n_list.append(n[length-1])                              #先加入第一個商品
    w = n[length-1][1][1]
    for i in range(length-2,-1,-1):                         #貪婪選商品
        if n[i][1][1]+w <= max_w:                           #所選商品可放入背包
            n_list.append(n[i])                             #加入貪婪背包
            w+=n[i][1][1]                                   #新的背包重量
    return n_list

n = {"iWatch手錶":(15000,0.1),                              #定義商品
     "Asus  筆電":(35000,0.7),
     "iPhone手機":(38000,0.3),
     "Acer  筆電":(40000,0.8),
     "Go Pro攝影":(12000,0.1),
    }

max_w = 1
th = sorted(n.items(), key=lambda item:item[1][0])            #商品依價值排序
print("所有商品依價值排序如下")
print("商品", "      商品價格", " 商品重量")
for i in range(len(th)):
    print(f"{th[i][0]:8s}{th[i][1][0]:10d}{th[i][1][1]:10.2f}")

t = greedy(th)                                                #呼叫貪婪選商品
m=0
print("貪婪選擇商品如下")
print("商品", "      商品價格", " 商品重量")
for i in range(len(t)):
    print(f"{t[i][0]:8s}{t[i][1][0]:10d}{t[i][1][1]:10.2f}")
    m+=t[i][1][0]
print(f"產品價值:{m}")