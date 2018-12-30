#!/usr/bin/python3
#文件：生成翻转棋子游戏数据
#作者：巧若拙
#日期：2018年12月30日

def turn(a, i, size):#翻转棋盘a中位置i及其周围的棋子
    a[i] = not a[i] #翻转位置i的棋子
    if i >= size:    
        a[i-size] = not a[i-size] #不是第一行则翻转上方棋子
    if i < size*(size-1):
        a[i+size] = not a[i+size] #不是第size行则翻转下方棋子
    if i % size > 0:
        a[i-1] = not a[i-1] #不是第一列则翻转左方棋子
    if (i+1) % size > 0:
        a[i+1] = not a[i+1] #不是第size列则翻转右方棋子

def change(c):
    if c:
        return "b"
    else:
        return "w"

def main():
    a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    b = [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
         [1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],
         [1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
         [0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0],
         [0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0],
         [1,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0],
         [0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1],
         [1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    with open('fzqz.in', 'w') as fout:
        for d in b:
            print(d)
            c = a.copy()
            for i in range(len(d)):
                if d[i] == 1: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
                    turn(c, i, size)
            c = "".join(list(map(change, c)))#生成黑白棋子棋盘
            print(c)
            fout.writelines(c[0:4]+"\n")
            fout.writelines(c[4:8]+"\n")
            fout.writelines(c[8:12]+"\n")
            fout.writelines(c[12:]+"\n")

size = 4 #4*4的方阵
main()
