def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    for i in range(int(input()) - 1, 1, -1):
        if prime(i):
            print(i)
            break