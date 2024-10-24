def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 :
            return False
        
    return True

def prime_list(n):
    return [num for num in range(2, n + 1) if prime(num)]

for _ in iter(input,'0'):
    target = int(_)
    count = 0
    num = set()
    lst = prime_list(target)
    for i in lst:
        if (target - i) in lst and (target - i) not in num:
            num.add(i)
            num.add(target - i)
            count += 1
    print(count)