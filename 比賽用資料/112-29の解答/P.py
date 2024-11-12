mat = [list(map(int, input().split())) for _ in range(3)]

a, b, c = map(sum, mat)
s = (a + b + c) // 2
a, b, c = s - a, s - b, s - c

mat[0][0] = a
mat[1][1] = b
mat[2][2] = c

for row in mat:
    print(*row)
