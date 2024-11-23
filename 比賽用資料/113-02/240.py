s = list(input())
check = 1
# 97, 122 
# 65, 90
#49 57
if any(chr(x) in s for x in range(97, 123)) and any(chr(x) in s for x in range(65, 91)) and any(chr(x) in s for x in range(49, 58)):
    first_low, first_up = 0, 0
    for i in range(len(s)):
        if s[i].islower() and first_low == 0:
            first_low = i
        elif s[i].isupper() and first_up == 0:
            first_up = i
    if first_low > first_up:
        check = 0
else:
    check = 0
print(check)