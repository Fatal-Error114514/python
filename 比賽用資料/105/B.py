code = {'-----':0, '.----':1, '..---':2, '...--':3, '....-':4, '.....':5, '-....':6, '--...':7, '---..':8, '----.':9}
for _ in range(int(input())):
    c = input().split()
    for i in c:
        print(code[i],end = '')
    print()