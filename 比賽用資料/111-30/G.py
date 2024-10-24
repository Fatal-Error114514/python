for _ in range(int(input())):
    s = input()
    new_string = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        if num:
            new_string += char * int(num)
    print(new_string)