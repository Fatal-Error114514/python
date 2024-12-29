from decimal import Decimal

# 不能用round, 因為round是使用bankers rounding, 會有一半的機率會錯誤
for _ in range(int(input())):
    s = Decimal(input()).quantize(Decimal('0.01'), rounding='ROUND_HALF_UP')
    if s == 0.00:
        print('0.00')
    else:
        print(s)