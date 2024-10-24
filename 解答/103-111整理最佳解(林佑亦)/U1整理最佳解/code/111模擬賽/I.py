from sys import stdin

def Input():
    return stdin.readline().rstrip()

#26進位
for _ in range(int(Input())):
    total = 0
    pw = 0
    n = Input()
    for i in n[::-1]:
        i = ord(i) - 64
        total += i * (26**pw)
        pw += 1
    print(total)






