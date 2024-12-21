s = input()
strong = 0
lower = 0
upper = 0
digit = 0
special = 0
for i in s:
    if i.islower() and lower == 0:
        lower += 1
    elif i.isupper() and upper == 0:
        upper += 1
    elif i.isdigit() and digit == 0:
        digit += 1
    elif not i.isalnum() and special == 0:
        special += 1
if len(s) >= 8:
    strong += 1
print(strong + lower + upper + digit + special)