#110商業技藝競賽模擬試題
#Problem B1 閏年
#Author: Yotrew Wing
#2021/10/18

year=int(input())
if year % 400 == 0:
    print("a leap year")
elif year % 4 ==0 and year % 100 !=0:
    print("a leap year")
else:
    print("a normal year")
