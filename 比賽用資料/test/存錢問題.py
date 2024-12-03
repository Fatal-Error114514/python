# 題目: 給一個天數，求出共存多少錢，第一個禮拜第一天存1、第二天存2...第七天存7;
# p.s 每個禮拜第一天的錢存的比上個禮拜多1塊

days = int(input())
weeks = days // 7
remaining_days = days % 7

# 完整週的總存款
total_weeks = 7 * (weeks * (weeks + 1)) // 2 + 21 * weeks

# 剩餘天數的總存款
remaining_sum = remaining_days * weeks + (remaining_days * (remaining_days + 1)) // 2

print(total_weeks + remaining_days)