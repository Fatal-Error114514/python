sign = [
    (1, 21, 2, 19, 'Aquarius'),
    (2, 20, 3, 20, 'Pisces'),
    (3, 21, 4, 20, 'Aries'),
    (4, 21, 5, 21, 'Taurus'),
    (5, 22, 6, 21, 'Gemini'),
    (6, 22, 7, 22, 'Cancer'),
    (7, 23, 8, 21, 'Leo'),
    (8, 22, 9, 23, 'Virgo'),
    (9, 24, 10, 23, 'Libra'),
    (10, 24, 11, 22, 'Scorpio'),
    (11, 23, 12, 22, 'Sagittarius'),
    (12, 23, 1, 20, 'Capricorn')
]

for _ in range(int(input())):
    m, d = map(int,input().split('/'))
    for start_m, start_d, end_m, end_d, star in sign:
        if m == start_m and d >= start_d or m == end_m and d <= end_d:
            print(star)
            break
