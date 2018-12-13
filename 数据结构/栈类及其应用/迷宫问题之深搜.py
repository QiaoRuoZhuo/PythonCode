#!/usr/bin/python3
# 文件名: StackClass.py
from StackClass import ListStack,LinkStack

OPEN, CLOSE, PASSED, ROAD = 0, 1, 2, -1 #分别表示该点通，不通，已走和属于所选路径
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0)) #分别向东南西北走的行列坐标变换情况

def mark(maze, pos):
    maze[pos[0]][pos[1]] = PASSED

def passable(maze, pos):    #判断当前位置是否可通行
    return maze[pos[0]][pos[1]] == OPEN

def find_path(maze, pos, end): #递归算法
    mark(maze, pos)
    if pos == end:
        print(pos, end = " ")
        return True
    for i in range(4):
        nextp = (pos[0]+dirs[i][0], pos[1]+dirs[i][1])
        if passable(maze, nextp) and find_path(maze, nextp, end):
            print(pos, end = " ")
            return True
    return False

def print_path(end, pos, s):#逆序输出路径
    print(end, end = " ")
    print(pos, end = " ")
    while not s.is_empty():
        print(s.pop()[0], end = " ")

def deepSearch(maze, start, end): #非递归算法
    if start == end:
        print(start)
        return True
    s = LinkStack()
    mark(maze, start)
    s.push((start, 0))
    while not s.is_empty():
        pos, nxt = s.pop()
        for i in range(nxt, 4): #依次检查未探查方向
            nextp = (pos[0]+dirs[i][0], pos[1]+dirs[i][1])
            if nextp == end:
                print_path(end, pos, s) #输出路径，注意此时end和pos不在栈中，需要单独输出
                return True
            if passable(maze, nextp):
                s.push((pos, i+1)) #原位置和下一方向入栈
                mark(maze, nextp)
                s.push((nextp, 0)) #新位置入栈
                break            #退出内层循环，处理下一位置
    return False


maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
        [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
        [1,0,1,0,0,0,0,1,0,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
        [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
        [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
start = (1, 1)                                       
end = (10, 12)
find_path(maze, start, end)
print()
maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
        [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
        [1,0,1,0,0,0,0,1,0,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
        [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
        [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
deepSearch(maze, start, end)
    
