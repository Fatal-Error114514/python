#103商業技藝競賽正式試題
#Problem 4： 資料結構—樹、陣列 子題 1：凱撒密碼。(程式執行限制時間: 2 秒)
#Author:Yotrew
#20210713
'''
建表:二進位,凱撒密文字母表(可以直接使用mod)
00 0
01 1  <---0個1為2位數
100 2
101 3 <---連續1個1為3位數,1之後還有2位
1100 4
1101 5 <---連續2個1為4位數,1之後還有2位
11100 6
11101 7 <---連續3個1為4位數,1之後還有2位
111100 8
111101 9 <---連續3個1為4位數,1之後還有2位
'''
#print(fib)
n=int(input())
bin_table={"00":0,"01":1,"100":2,"101":3,"1100":4,"1101":5,"11100":6,
           "11101":7,"111100":8,"111101":9}

for i in range(0,n):
    x=input().strip()
    bin_2_dec=0#剖出2進位的各個位數變成10進位數
    #bin=[]
    a=0
    tmp=""

    while a<len(x):
        if x[a]=="0":
            tmp+=x[a]+x[a+1]
            #bin.append(bin_table[tmp])
            bin_2_dec=bin_2_dec*10+bin_table[tmp]
            tmp=""
            a+=1
        else:
            tmp+=x[a]
        a+=1
    '''for a in range(1,27):
        print(a,chr(65+(a+2)%26))'''
    print(chr(65+(bin_2_dec+2)%26))
        
