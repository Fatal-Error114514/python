for _ in iter(input,'0 0'):
    a, b = map(int,_.split())
    carry = 0
    carry_count = 0
    while a > 0 or b > 0:
        d1 = a % 10
        d2 = b % 10
        if d1 + d2 + carry >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
        a //= 10
        b //= 10
    if carry_count > 1:
        print(f'{carry_count} carry operations.')
    elif carry_count == 1:
        print('1 carry operation.')
    else:
        print('No carry operation.')