import bisect

for _ in range(int(input())):
    n = int(input())
    red, blue = [], []

    for i in range(n):
        f = int(input())
        if f > 0:
            blue.append(f)
        else:
            red.append(-f)
    red.sort()
    blue.sort()

    ans = 1
    ir, ib = 0, 0
    if len(red) > 0 and len(blue) > 0:
        # 確定初始值
        if red[0] < blue[0]:
            b = True    # 紅色開始
            now = red[0]
        else:
            b = False   # 藍色開始
            now = blue[0]

        # 紅藍交替選擇
        while ir < len(red) and ib < len(blue):
            if b:   # 目前需要找藍色
                ib = bisect.bisect_right(blue, now)
                if ib < len(blue):
                    now = blue[ib]
                    b = False
                    ans += 1
            else:   # 目前需要找紅色
                ir = bisect.bisect_right(red, now)
                if ir < len(red):
                    now = red[ir]
                    b = True
                    ans += 1
        print(ans)
    else:
        print(ans)