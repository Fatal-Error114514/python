import math
# 先找到a, b, 接著在減a**2 & b ** 2, 看剩下的數字是否在集合中
def find_three_squares(x):
    squares = [i * i for i in range(int(math.sqrt(50000)) + 1)]
    square_set = set(squares)
    
    # 遍歷所有可能的 a 和 b
    for a in range(int(math.sqrt(x)) + 1):
        for b in range(a, int(math.sqrt(x - a * a)) + 1):
            remaining = x - a * a - b * b
            if remaining in square_set:
                c = int(math.sqrt(remaining))
                return a, b, c
    return -1

for _ in range(int(input())):
    x = int(input())
    result = find_three_squares(x)
    if result == -1:
        print(result)
    else:
        print(result[0], result[1], result[2])