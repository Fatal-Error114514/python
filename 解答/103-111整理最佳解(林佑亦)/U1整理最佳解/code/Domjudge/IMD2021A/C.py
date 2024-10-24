output = []
n = int(input())
while n:
    output.append(n)
    temp = []
    for i in range(n):
        temp.append(input())
    n = int(input())
    output += [' '.join(temp)]
print(*output, sep='\n')
