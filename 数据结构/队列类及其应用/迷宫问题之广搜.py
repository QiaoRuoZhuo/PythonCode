#!/usr/bin/python3
# 文件名: StackClasq.py
# 作者: 巧若拙
# 日期: 2018年12月14日
from QueueClass import ListQueue,LinkQueue

OPEN, CLOSE, PASSED, ROAD = 0, 1, 2, -1 #分别表示该点通，不通，已走和属于所选路径
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0)) #分别向东南西北走的行列坐标变换情况

def mark(maze, pos):
    maze[pos[0]][pos[1]] = PASSED

def passable(maze, pos):    #判断当前位置是否可通行
    return maze[pos[0]][pos[1]] == OPEN


def print_path(start, end, path):#逆序输出路径
    print(end, end = " ")
    pos = path[end]
    while path[pos] != pos:
        print(pos, end = " ")
        pos = path[pos]
    print(start)

def extentSearch(maze, start, end): #用队列实现广度优先搜索
    if start == end:
        print(start)
        return True
    q = LinkQueue()
    mark(maze, start)
    q.enqueue(start)
    path = {start: start} #用字典记录其前驱位置
    while not q.is_empty():
        pos = q.dequeue()
        for i in range(4): #依次检查四个方向
            nextp = (pos[0]+dirs[i][0], pos[1]+dirs[i][1])
            if passable(maze, nextp):
                mark(maze, nextp)
                q.enqueue(nextp)
                path[nextp] = pos
                if nextp == end:
                    print_path(start, end, path)
                    return True
        
    return False

start = (1, 1)                                       
end = (10, 12)
maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
        [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
        [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
print(extentSearch(maze, start, end))
