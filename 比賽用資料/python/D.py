from bisect import bisect


print([0, 1, 0, 2, 0][bisect([65, 91, 97, 123], int(input()))])
