#106商業技藝競賽正式試題
#Problem 3：數學問題 子題 1：網段廣播位址
'''
2進位運算和10進位運算沒什麼不同
題目已告訴你運算方式,所以就直接使用位元運算
python:#Ref:http://kaiching.org/pydoing/py/python-bitwise.html
<<	向左位移
>>	向右位移
&	位元且
|	位元或
^	位元互斥或
~	位元非
#同108術科模擬試題Problem 3-2
'''

n=int(input())

for i in range(0,n):
    in_str=input().strip().split("/")
    ip=list(map(int,in_str[0].split(".")))
    netmask=list(map(int,in_str[1].split(".")))
    #print(ip)
    #print(netmask)
    mask_len=0
    for a in range(0,3):
        print(256+(ip[a] |( ~netmask[a])),end=".")
    print(256+(ip[3] |( ~netmask[3])))
    #print(ip[a] & netmask[a])
    