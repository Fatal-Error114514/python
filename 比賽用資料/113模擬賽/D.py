for i in iter(input, '0'):
    n = int(i)
    lst = list(map(int, input().split()))
    lst.sort()
    cost = 0
    while len(lst) > 3:
        # 策略1: 最快兩個人先過橋，最快的人返回，最慢的兩人過橋，次快的人返回
        method1 = lst[0] + lst[1]*2 + lst[-1]
        # 策略2: 最快的人帶最慢的兩人過橋，最快的人返回，次慢的兩人過橋，最快的人再次返回
        method2 = lst[0] * 2 + lst[-1] + lst[-2]

        cost += min(method1, method2)
        lst = lst[:-2]
    if len(lst) == 3:
        cost += lst[0] + lst[1] + lst[2]
    elif len(lst) == 2:
        cost += lst[1]
    else:
        cost += lst[0]
    print(cost)
"""
11 7 4 2 1
() 表示移動

11 7 4     -> (2 1)            cost 2
11 7 4 (1) <- 2                cost 1
4 1        -> 2 (11 7)         cost 11
4 1 (2)    <- 11 7             cost 2
2          -> 11 7 (4 1)       cost 4
2 (1)      <- 11 7 4           cost 1
None       -> 11 7 4 (2 1)     cost 2

total: 2 + 1 + 11 + 2 + 4 + 1 + 2 = 23

移動方式:
1. 最快兩個一起走，最快的回來
2. 最慢兩個一起走，山洞裡最快的回來(前提是山洞要有人)
3. 最快帶最慢，最快的回來
"""