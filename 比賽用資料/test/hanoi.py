#A:起始點
#B:中介點
#C:目的地
#一次只能拿一個圓盤，小圓盤一定要在大圓盤上面
#n-1的圓盤搬走(中介點)
def hanoi(n,A,B,C):
    if n==1:
        print(f"move disk {n} from {A} to {C}")
    else:
        hanoi(n-1,A,C,B)    #A->B
        print(f"move disk {n} from {A} to {C}")
        hanoi(n-1,B,A,C)    #B->C

hanoi(int(input()),"A","B","C")