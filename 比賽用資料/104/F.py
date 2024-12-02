for _ in range(int(input())):
    m, r, r, n = eval(input())
    A = [list(map(int,input().split())) for i in range(m)]
    B = [list(map(int,input().split())) for i in range(r)]
    AB = [list(map(int,input().split())) for i in range(m)]
    in_A = any(9999 in i for i in A)

    if in_A:    # case A
        for i in range(m):
            if 9999 in A[i]:
                row = i
                temp = A[row].index(9999)
                for j in range(n):      # 在B裡面找到9999的係數，係數不為0
                    if B[temp][j] != 0:
                        col = j
                        break
                break
        ans = 0
        div = 0
        for p, q in zip(A[row], list(zip(*B))[col]):
            if p != 9999:
                ans += p * q
            else:
                div = q

    else:       # case B
        for i in range(r):
            if 9999 in B[i]:
                col = B[i].index(9999)
                for j in range(m):      # 在A裡面找9999的係數，不能為0
                    if A[j][i] != 0:
                        row = j
                        break
                break
        div = 0
        ans = 0
        for p, q in zip(A[row], list(zip(*B))[col]):
            if q != 9999:
                ans += p * q
            else:
                div = p

    print((AB[row][col] - ans) // div)