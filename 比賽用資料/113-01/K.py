nums = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
for _ in range(int(input())):
    n, code = map(int,input().split())
    ans = ''
    while n > 0:
        temp = str(n % code) if n % code < 10 else nums[n % code]
        ans = temp + ans
        n //= code
    print(ans if ans else 0)