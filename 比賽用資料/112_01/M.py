k = 1
for _ in range(int(input())):
    n = input()
    visited = []
    print(f'Case #{k}: {n} ', end = '')
    while n != '1':
        n = str(sum(map(lambda x: int(x) ** 2, n)))
        if n in visited:
            print('is an Unhappy number.')
            break
        visited.append(n)
    else:
        print('is a Happy number.')
    k += 1