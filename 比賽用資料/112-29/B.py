n=list(map(str,input().split()))
if n[0]==n[1]:
    print(0)
elif n[0]=="Y" and n[1]=="O":
    print(2)
elif n[0]=="Y" and n[1]=="X":
    print(1)
elif n[0]=="O" and n[1]=="Y":
    print(1)
elif n[0]=="O" and n[1]=="X":
    print(2)
elif n[0]=="X" and n[1]=="Y":
    print(2)
else:
    print(1)