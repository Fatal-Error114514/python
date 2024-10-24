def odd(nums):
    odds = [i for i in nums if i % 2 != 0]
    return min(odds)
n = int(input())
num = list(map(int,input().split()))
if sum(num) % 2 != 0:
    m = odd(num)
    num.remove(m)
    print(sum(num))
else:
    print(sum(num))