s = input().split()
nums = eval(s[-1])
for i in nums:
    if nums.count(i) >= 2:
        print('true')
        break
else:
    print('false')