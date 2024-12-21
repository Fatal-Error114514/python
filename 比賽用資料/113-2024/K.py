for _ in range(int(input())):
    is_negative = False
    n = input()
    interger, decimal = n.split('.')
    if '-' in interger:
        is_negative = True
        interger = interger[1:]
    while len(decimal) < 3:
        decimal += '0'
    decimal += '0'
    if decimal[2] >= '5':
        if decimal[1] == '9':
            if decimal[0] == '9':
                interger = str(int(interger) + 1)
                decimal = '00'
            else:
                decimal = str(int(decimal[0]) + 1) + '0'
        else:
            decimal = decimal[0] + str(int(decimal[1]) + 1)
    if is_negative and int(interger) != 0 and int(decimal[:2]) != 0:
        print('-' + interger + '.' + decimal[:2])
    else:
        print(interger + '.' + decimal[:2])