for _ in range(int(input())):
        n = input().split()
        n = [list(i) for i in n]
        count = 0
        for i in n:
            if 's' in i or 'S' in i:
                  count += 1
        print(f'{len(n)},{count}')