def lcs(string):
    if not string:
        return ''
    common = string[0]
    for s in string[1:]:
        temp = ''
        longest = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = common[i:j]
                if sub in s and len(sub) > longest:
                    longest = len(sub)
                    temp = sub
        
        common = temp
        if not common:
            break
    return common

string = []
try:
    while True:
        s = input().strip()
        if s: string.append(s)
except EOFError:
    pass
print(lcs(string))