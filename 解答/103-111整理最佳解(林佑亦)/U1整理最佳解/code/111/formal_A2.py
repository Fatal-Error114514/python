n = int(input())
while n:
    if(n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
        print('a leap year')
    else:
        print('a normal year')

    n = int(input())
