from sys import stdin

def Input():
    return stdin.readline().rstrip()

dic = {
    '-----':0,
    '.----':1,
    '..---':2,
    '...--':3,
    '....-':4,
    '.....':5,
    '-....':6,
    '--...':7,
    '---..':8,
    '----.':9}
for _ in range(int(Input())):
    lst = Input().split()
    for i in lst:
        print(dic[i],end='')
    print()

    