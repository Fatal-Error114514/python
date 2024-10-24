from sys import stdin

def Input():
    return stdin.readline().strip()

sky = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
floor  = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
animal = ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬']

n = Input()
while n:
    n = int(n) - 73
    a = n % 10
    b = n % 12
    print(f'{sky[a]}{floor[b]},{animal[b]}年')

    n = Input()
