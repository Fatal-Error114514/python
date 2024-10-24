from pprint import pprint
maze = [
        [1, 1, 1, 1, 1, 1],                     #迷宮地圖
        [1, 0, 1, 0, 1, 1],                     # 1 代表牆， 0 代表通道
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1]
        ]
direct=[                                        #用串列設計迷宮方向
        lambda x,y: (x-1,y),                    #往上走
        lambda x,y: (x+1,y),                    #往下走
        lambda x,y: (x,y-1),                    #往左走
        lambda x,y: (x,y+1)                     #往右走
        ]
def solve(x,y,goalx,goaly):
    "解迷宮程式 x,y 是迷宮入口, goalx,goaly 是迷宮出口"
    maze[x][y]=2
    stack=[]                                    #建立路徑堆疊
    stack.append((x,y))                         #將路徑push進堆疊
    print("迷宮開始")
    while (len(stack)>0):
        cur=stack[-1]                           #目前位置  (n[-1]會回傳串列最後一個值)
        if cur[0] == goalx and cur [1] == goaly:
            print("抵達出口")
            pprint(stack)
            return True                         #抵達出口返回True
        for i in direct:                        #依上,下,左,右優先次序走出迷宮
            next=i(cur[0],cur[1])
            if maze[next[0]][next[1]]==0:       #如果是通道可以走
                stack.append(next)
                maze[next[0]][next[1]]=2        #用2標記可以走的路
                break
        else:                                   #如果進入死路，則回朔
            maze[cur[0]][cur[1]]=3              #標記死路
            stack.pop()                         #回朔
        print(f"目前位置:{cur}")
    else:
        print("沒有路徑")
        return False
solve(1,1,4,4)
pprint(maze)                                    #跳行顯示路徑