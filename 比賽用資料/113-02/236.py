s = input()
if all(s[i - 1] < s[i] for i in range(2, len(s))):
    print(1)
elif all(s[i - 1] > s[i] for i in range(1, len(s) - 1)):
    print(2)
else:
    print(3)