def gary(n):
    if(n == 1):
        return ['0', '1']
    lst = gary(n-1)
    output = []
    for i in lst:
        output.append('0' + i)
    for i in lst[::-1]:
        output.append('1' + i)
    return output




n = int(input())
print(*gary(n),sep='\n')