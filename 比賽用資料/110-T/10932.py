#first date 1970-01-01
from datetime import datetime, timedelta

date = datetime(1970, 1, 1)
for _ in range(int(input())):
    day = int(input())
    new = date + timedelta(days = day)
    print(new.strftime('%Y-%m-%d'))