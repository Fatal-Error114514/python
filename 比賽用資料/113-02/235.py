n = list(input())
b = max(i for i in n)
print(1 if n.index(b) != 0 and n.index(b) != len(n) - 1 and n.count(b) == 1 else 0)