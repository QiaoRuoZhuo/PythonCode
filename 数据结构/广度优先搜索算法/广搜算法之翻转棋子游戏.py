#!/usr/bin/python3
#文件：广搜算法之翻转棋子游戏
#作者：巧若拙
#日期：2018年12月26日
'''
题目描述
翻转游戏是这样玩的：
有一张4*4的棋盘，在16个位置上每个位置放着一个棋子，棋子一面是黑色，另一面是白色，棋子或者白色面朝上，或者黑色面朝上。
游戏的走法如下：每一步先选择一个位置，然后把该位置和上，下，左，右（不越界）相邻位置上的棋子翻转（白->黑，黑->白）。
我们用w表示棋子白色面朝上，b表示黑色面朝上。
例如：考虑如下棋盘状态：
bwbw
wwww
bbwb
bwwb
当我们选择第三行，第一列的位置翻转时，棋盘变化为:
bwbw
bwww
wwwb
wwwb
游戏的目的是用最少的步数把全部棋子变为白色向上或黑色向上。
时限：1s。

输入格式
4行由b和w组成的字符串描述的一个棋盘的初始状态。

输出格式
一个测试数据输出一行，为所需要的最少的翻转次数，如果无法翻转成目标状态，则输出’impossible’（小写，没有引号）。

样例输入（1）
bwbw
wwww
bbwb
bwwb

样例输出（1）
Impossible

样例输入（2）
bwwb
bbwb
bwwb
bwww

样例输出（2）
4
'''

from queue import Queue

def check(a):#判断是否已经翻转成功:全部棋子变为白色向上或黑色向上
    return all(a) or not any(a)

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


def exhaustion(a): #穷举法解翻转棋子游戏
    min_c = len(a) #初始化最小步数，每个棋子都翻转
    for t in range(1<<len(a)):#遍历从[0,1<<len(a)]的所有翻转模式
        b, c = a.copy(), 0 #复制棋盘a到b，c用来累计翻转棋子的数量
        for i in range(len(lib)):
            if t & lib[i] > 0: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
                turn(b, i, size)
                c += 1
        if check(b) and c < min_c:#本翻转模式能获得更好的解，则更新最优解
            min_c = c
    return min_c


'''
广搜法：把各种翻转模式存储到队列中，翻转棋子的数量从小到大依次加入队列。
一开始设置翻转棋子数为0，然后逐渐增加翻转棋子数量（通过按位或运算实现）。
为避免重复，每次增加的翻转棋子的位置只能出现在当前模式的右侧，
可以遍历lib，将其元素与代表当前翻转模式的整数t依次进行按位或运算，直到结果等于t，
相当于从右向左依次修改0为1，直到遇到1，这样可以确保只在原数的右侧增加1个1。
将每次按位或运算的结果就是在当前模式的右侧位置增加一个翻转棋子的模式，将其加入队列即可。
因为翻转棋子的数量越来越多，故最早获得的解就是最优解。
'''
def bfs(a): #广搜法解翻转棋子游戏
    q = Queue() #创建队列对象
    q.put(0) #翻转棋子数为0
    while not q.empty():
        t = q.get()
        b, c = a.copy(), 0 #复制棋盘a到b，c用来累计翻转棋子的数量
        for i in range(len(lib)):
            if t & lib[i] > 0: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
                turn(b, i, size)
                c += 1
        if check(b): #因为翻转棋子的数量越来越多，故最早获得的解就是最优解
            return c
        else:
            for x in lib:
                if t != t | x:#从右向左依次修改0为1，直到遇到1，这样可以确保只在原数的右侧增加1个1
                    q.put(t | x)
                else:
                    break
    return len(a) #无解则返回len(a)


def main():
    a = []
    with open('fzqz.in', 'r') as fin:
        for line in fin.readlines():
            print(line.strip())#依次读取每行  
            a.extend(line.strip()) #去掉每行头尾空白 
    a = list(map(lambda x: x=="b", a))
    '''
    min_c = exhaustion(a)
    if min_c < len(a):
        print(min_c)
    else:
        print("impossible")
    '''
    min_c = bfs(a)
    if min_c < len(a):
        print(min_c)
    else:
        print("impossible")
    #'''

size = 4 #4*4的方阵
lib = tuple(map(lambda x: 1 << x, range(size**2)))#标记每个二进制位的1
print(lib)
main()



