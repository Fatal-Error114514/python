def is_vaild(l):
    fill = [n for n in l if n != '?']
    return len(fill) != len(set(fill))

def sudoku():
    lst = []
    nums = [str(i) for i in range(1, 10)]

    for i in range(9):
        n = input().split(',')
        if is_vaild(n) or is_vaild(list(zip(n))):
            return -1
        lst.append(n)

    for i in range(9):
        if '?' in lst[i]:
            x = lst[i].index('?')
            y = i

    start_row = (y // 3) * 3
    start_col = (x // 3) * 3
    end_row = start_row + 3
    end_col = start_col + 3
    martix = []
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            martix.append(lst[i][j])
    row = list(list(zip(*lst))[x])
    col = lst[y]
    for i in nums:
        if i not in row and i not in col and i not in martix:
            return i

print(sudoku())