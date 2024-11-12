a, b = input().split()

mapping = {'Y': 0, 'O': 1, 'X': 2}
matrix = [[0, 2, 1], [1, 0, 2], [2, 1, 0]]

print(matrix[mapping[a]][mapping[b]])
