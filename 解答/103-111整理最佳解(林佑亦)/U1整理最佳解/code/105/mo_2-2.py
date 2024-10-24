from sys import stdin

data = stdin.read()
a = data.count('\n')
b = len(data.replace('\n', ' ').split())
c = len(data.replace('\n', ''))
print(a,b,c, sep=',')

