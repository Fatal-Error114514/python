for i in iter(input,'0'):
    n = int(i)
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print('a leap year')
    else:
        print('a normal year')