abc = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
try:
    count = 0
    while True:
        n = input().split()
        for i in n:
            word_count = 0
            for j in i:
                if j in abc: word_count += 1
            if word_count == 2:
                count += 1
except EOFError:
    pass
print(count)