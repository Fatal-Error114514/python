while True:
    try:
        n = input()
        if n:
            b = 0
            a = 1
            for i in range(len(n)):
                b += int(n[i]) * a
                if i == 0: continue
                a *= -1
            print(b)
        else:
            break
    except:
        break