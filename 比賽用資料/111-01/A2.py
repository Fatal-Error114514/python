a, b = sorted([int(input()), int(input())])
for i in range(a + 1, b):
    if i % 5 == 2 or i % 5 == 3:
        print(i)