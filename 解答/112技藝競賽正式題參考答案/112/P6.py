ss = input().replace(',', ' ').replace('.', ' ').split()

def check(s):
    return s.upper() == s or s.lower() == s or s[0].upper() == s[0] and s[1:].lower() == s[1:]

print(int(all(map(check, ss))))
