for _ in range(int(input())):
    n = int(input())

    ans = 0
    s_prime = '#' + input() + '##'
    print(sum(s_prime[i + 2] != s_prime[i] for i in range(n - 1)))