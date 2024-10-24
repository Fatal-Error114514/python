def check(name):
    if voted[name]:
        print("你已經投過票了")
    else:
        print("歡迎投票")
        voted[name]=True
voted={"trump":False,"lisa":False,"mike":False}
for i in range(3):
    name=input("請輸入名字:")
    if name in voted:
        check(name)
    else:
        print("你不是選民")