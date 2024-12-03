# 題目: 給一個數列，求符合要求的子數列數(子數列包含輸入的max_k 跟 min_k)

def count_subarrays_with_min_max(arr, min_val, max_val):
    n = len(arr)
    left = 0
    count = 0
    min_pos = -1
    max_pos = -1

    # 遍歷整個數組
    for right in range(n):
        # 當右指針指向最小值或最大值時，更新對應的位置
        if arr[right] == min_val:
            min_pos = right
        if arr[right] == max_val:
            max_pos = right

        # 當窗口內同時包含最小值和最大值時，更新計數
        if min_pos != -1 and max_pos != -1:
            # 當最小值和最大值都出現時，從 left 到 right 的所有子串列都滿足條件
            count += min(min_pos, max_pos) - left + 1

    return count

# 用戶輸入數據
arr = list(map(int, input("請輸入一個整數數組，用空格分隔: ").split()))
min_val = int(input("請輸入最小值: "))
max_val = int(input("請輸入最大值: "))

# 計算符合條件的子串列數量
result = count_subarrays_with_min_max(arr, min_val, max_val)
print(f"符合條件的子串列數量是: {result}")
# 輸出結果