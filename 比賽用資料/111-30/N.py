def longest(n, score):
    if len(score) == 0: return 0
    array = [1] * (n + 1)
    for i in range(1, n):
        for j in range(i):
            if score[j] < score[i]:
                array[i] = max(array[i], array[j] + 1)

    return max(array)


n = int(input())
score = list(map(int,input().split()))
print(longest(n, score))