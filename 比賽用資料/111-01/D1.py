from collections import Counter
while True:
    try:
        a = input()
        b = input()
        count = Counter(a) & Counter(b)
        k = sorted(count.keys())
        b = ''
        for i in k:
            for j in range(count[i]):
                b += i
        print(b)
    except:
        break