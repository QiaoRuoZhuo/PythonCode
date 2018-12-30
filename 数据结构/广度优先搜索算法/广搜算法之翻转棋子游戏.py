#!/usr/bin/python3
#文件：广搜算法之翻转棋子游戏
#作者：巧若拙
#日期：2018年12月30日
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

算法分析：
初看本题，最容易想到的是穷举法，用包含16个元素的列表d分别表示每个棋子的翻转状态，d[i]=1表示翻转第i个棋子，d[i]=0表示不翻转。
可以穷举从d=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]到d=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]，即从都不翻转到都翻转。
若把列表d的值对应整数t的16位二进制数，则相当于穷举从t=0到t=2^16-1。
比较直白的算法是循环遍历每一个t，将t的16位二进制数存储到列表d；然后遍历d，若d[i]=1则翻转位置i及其周围的棋子，并计数；
完成本翻转模式后，判断是否有解，若本翻转模式能获得更好的解，则更新最优解。
上述算法思想简单明了，但把整数t转化成二进制数并存储到列表d的操作比较耗费时间。
我们可以使用位运算来处理整数t的二进制数，这样就无需引入列表d，可以直接操作整数t了，效率有所提升。
穷举法是容易想到的算法，但是效率实在太低，我们可以使用深度优先搜索（回溯加剪枝）来实现同样的功能。
更进一步思考，既然题目要求的是最优解，我们应该使用广度优先搜索才是效率更高的做法。
为避免翻转模式重复入队列，常见的算法是设置一个长度为2^16的列表f，用来标记整数t是否出现过，先初始化f[i]=False，一旦整数i入队列，则设置f[i]=True；
但是我没有使用这种方法，而是规定每次只在当前翻转模式的左侧增加翻转的棋子，这样就能避免重复。
这样我们就分别用穷举，深搜和广搜三种算法实现了所需功能。
回到最初的想法，我们使用列表d来表示整数t的二进制数的每一位，是很直观的想法，只不过每次都需要把整数转化成二进制数比较耗费时间；
其实我们可以直接修改列表d的值来模拟整数t递增的过程，这样就不需要引入整数t及其位运算了，数据结构更清晰。
我也用这种数据结构实现了穷举，深搜和广搜三种算法。
'''

from queue import Queue

#判断是否已经翻转成功:全部棋子变为白色向上或黑色向上
def check(a):
    return all(a) or not any(a)

#翻转棋盘a中位置i及其周围的棋子
def turn(a, i, size):
    a[i] = not a[i] #翻转位置i的棋子
    if i >= size:    
        a[i-size] = not a[i-size] #不是第一行则翻转上方棋子
    if i < size*(size-1):
        a[i+size] = not a[i+size] #不是第size行则翻转下方棋子
    if i % size > 0:
        a[i-1] = not a[i-1] #不是第一列则翻转左方棋子
    if (i+1) % size > 0:
        a[i+1] = not a[i+1] #不是第size列则翻转右方棋子

#将整数t的16位二进制数存储到列表d
def binary_number(t, n): 
    d =[0] * n #高位补零，凑足n位
    i = n -1
    while t > 0:
        d[i] = t & 1         #相当于t % 2
        i, t = i - 1, t >> 1 #相当于t // 2
    return d

#穷举法解翻转棋子游戏：最直观的想法，把整数t的16位二进制数存储到列表d，并根据列表d的值来确定翻转模式
def exhaustion_0(a):  
    min_c = len(a) + 1 #初始化最小步数为最大值 
    for t in range(1<<len(a)): #遍历从[0,1<<len(a)]的所有翻转模式
        b, c = a.copy(), 0 #复制棋盘a到b，c用来累计翻转棋子的数量
        d = binary_number(t, len(a)) #将整数t的16位二进制数存储到列表d
        for i in range(len(d)):
            if d[i] == 1: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
                turn(b, i, size)
                c += 1
        if check(b) and c < min_c: #本翻转模式能获得更好的解，则更新最优解
            min_c = c
    return min_c

#穷举法解翻转棋子游戏：直接用位运算操作整数t的各个二进制数位，效率更高
def exhaustion_1(a):  
    min_c = len(a) + 1 #初始化最小步数为最大值 
    for t in range(1<<len(a)): #遍历从[0,1<<len(a)]的所有翻转模式
        b, c = a.copy(), 0 #复制棋盘a到b，c用来累计翻转棋子的数量
        for i in range(len(lib)):
            if t & lib[i] > 0: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
                turn(b, i, size)
                c += 1
        if check(b) and c < min_c: #本翻转模式能获得更好的解，则更新最优解
            min_c = c
    return min_c

#穷举法解翻转棋子游戏：直接修改列表d的值来模拟整数t递增的过程，无需进行位运算，更好理解
def exhaustion_2(a): 
    min_c = len(a) + 1 #初始化最小步数为最大值
    d =[0] * len(a) #初始化所有的位都是0
    while True: #遍历从[0,1<<len(a)]的所有翻转模式
        b, c = a.copy(), 0 #复制棋盘a到b，c用来累计翻转棋子的数量
        for i in range(len(d)):
            if d[i] == 1: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
                turn(b, i, size)
                c += 1
        if check(b) and c < min_c: #本翻转模式能获得更好的解，则更新最优解
            min_c = c
        i = len(d) - 1
        while i >= 0 and d[i] == 1: #修改列表d的值来模拟整数t递增的过程，每次递增1
            d[i] = 0
            i -= 1
        if i >= 0:  #将d[i]右侧的1都改成0，d[i]改成1，相当于二进制数递增1
            d[i] = 1
        else:  #已经递增到最大值，即所有的二进制位均为1
            break
    return min_c

'''
#2个不完全的回溯算法。说他们不完全回溯，是因为每次都是使用列表a的拷贝进入下一层递归函数的，并且每次都翻转了该模式中所有的棋子，与穷举法并无二致。
def dfs_3(a, t): #深搜法解翻转棋子游戏
    global min_cc
    b, c = a.copy(), 0 #复制棋盘a到b，c用来累计翻转棋子的数量
    for i in range(len(lib)):
        if t & lib[i] > 0: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
            turn(b, i, size)
            c += 1
    if check(b): #已经有解就不必再翻转更多棋子了
        if c < min_cc:#本翻转模式能获得更好的解，则更新最优解
            min_cc = c
    else:
        for x in lib:
            if t != t | x:#从左向右依次修改0为1，直到遇到1，这样可以确保只在原数的左侧增加1个1
                dfs_3(a, t | x)
            else:
                break

def dfs_4(a, d): #深搜法解翻转棋子游戏
    global min_cc
    b, c = a.copy(), 0 #复制棋盘a到b，c用来累计翻转棋子的数量
    for i in range(len(d)):
        if d[i] == 1: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
            turn(b, i, size)
            c += 1
    if check(b): #已经有解就不必再翻转更多棋子了
        if c < min_cc:#本翻转模式能获得更好的解，则更新最优解
            min_cc = c
    else:
        for i in range(len(d)):
            if d[i] == 0:#从左向右依次修改0为1，直到遇到1，这样可以确保只在原数的左侧增加1个1
                d[i] = 1
                dfs_4(a, d)
                d[i] = 0 #回溯
            else:
                break
'''
#深搜法解翻转棋子游戏：直接用位运算操作整数t的各个二进制数位，每层递归函数的棋盘都继承自上一层函数，每层只翻转1个棋子
#参数介绍：a——列表，存储当前棋盘状态；t——正整数，其二进制数代表当前翻转模式；c——正整数，表示已经翻转的棋子数量。
def dfs_1(a, t, c): 
    global min_cc
    if check(a): #已经有解就不必再翻转更多棋子了
        if c < min_cc:#本翻转模式能获得更好的解，则更新最优解
            min_cc = c
    else:
        for i in range(len(lib)):
            if t & lib[i] == 0: #从左向右依次修改0为1，直到遇到1，这样可以确保只在原二进制数的左侧增加1个1
                t |= lib[i]     #将整数t的第i个二进制位设置成1
                turn(a, i, size)
                dfs_1(a, t, c+1)
                turn(a, i, size)#回溯
                t &= ~lib[i]    #将整数t的第i个二进制位恢复成0
            else:
                break

#深搜法解翻转棋子游戏：使用列表d存储当前翻转模式，每层递归函数的棋盘都继承自上一层函数，每层只翻转1个棋子
#参数介绍：a——列表，存储当前棋盘状态；d——列表，存储当前翻转模式；c——正整数，表示已经翻转的棋子数量。
def dfs_2(a, d, c):  
    global min_cc
    if check(a): #已经有解就不必再翻转更多棋子了
        if c < min_cc:#本翻转模式能获得更好的解，则更新最优解
            min_cc = c
    else:
        for i in range(len(d)):
            if d[i] == 0:#从左向右依次修改0为1，直到遇到1，这样可以确保只在原二进制数的左侧增加1个1
                d[i] = 1
                turn(a, i, size)
                dfs_2(a, d, c+1)
                turn(a, i, size) #回溯
                d[i] = 0 #回溯
            else:
                break
            

'''
广搜法：把各种翻转模式存储到队列中，翻转棋子的数量从小到大依次加入队列。
一开始设置翻转棋子数为0，然后逐渐增加翻转棋子数量（通过按位或运算实现）。
为避免重复，每次增加的翻转棋子的位置只能出现在当前模式的左侧，
可以遍历lib，将其元素与代表当前翻转模式的整数t依次进行按位或运算，直到结果等于t，
相当于从左向右依次修改0为1，直到遇到1，这样可以确保只在原二进制数的左侧增加1个1。
每次按位或运算的结果就是获得新的翻转模式，将其加入队列即可。
因为翻转棋子的数量越来越多，故最早获得的解就是最优解。
'''
#广搜法解翻转棋子游戏：直接用位运算操作整数t的各个二进制数位，效率更高
def bfs_1(a):
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
            for i in range(len(lib)):
                if t & lib[i] == 0:  #从左向右依次修改0为1，直到遇到1，这样可以确保只在原二进制数的左侧增加1个1 
                    q.put(t | lib[i])#将整数t的第i个二进制位设置成1后入列
                else:
                    break
    return len(a)+1 #无解则返回len(a)+1

#广搜法解翻转棋子游戏：使用列表d存储当前翻转模式，较为直观
def bfs_2(a): 
    q = Queue() #创建队列对象
    d =[0] * len(a) #初始化所有的位都是0
    q.put(d) #翻转棋子数为0
    while not q.empty():
        d = q.get()
        b, c = a.copy(), 0 #复制棋盘a到b，c用来累计翻转棋子的数量
        for i in range(len(d)):
            if d[i] == 1: #t的二进制数第i位是1，则翻转位置i及其周围的棋子，并计数
                turn(b, i, size)
                c += 1
        if check(b): #因为翻转棋子的数量越来越多，故最早获得的解就是最优解
            return c
        else:
            for i in range(len(d)):
                if d[i] == 0:#从左向右依次修改0为1，直到遇到1，这样可以确保只在原二进制数的左侧增加1个1
                    t = d.copy()
                    t[i] = 1 
                    q.put(t) #生成列表d的拷贝，并将其第i个二进制位设置成1后入列
                else:
                    break
    return len(a)+1 #无解则返回len(a)+1


def main(a):
    min_c = exhaustion_0(a) #穷举法解翻转棋子游戏
    if min_c <= len(a):
        print(min_c)
    else:
        print("impossible")
        
    min_c = exhaustion_1(a) #穷举法解翻转棋子游戏
    if min_c <= len(a):
        print(min_c)
    else:
        print("impossible")

    min_c = exhaustion_2(a) #穷举法解翻转棋子游戏
    if min_c <= len(a):
        print(min_c)
    else:
        print("impossible")
     
    min_c = bfs_1(a) #广搜法解翻转棋子游戏
    if min_c <= len(a):
        print(min_c)
    else:
        print("impossible")

    min_c = bfs_2(a) #广搜法解翻转棋子游戏
    if min_c <= len(a):
        print(min_c)
    else:
        print("impossible")
    
    global min_cc
    min_cc = len(a)+1
    dfs_1(a, 0, 0) #深搜法解翻转棋子游戏
    if min_cc <= len(a):
        print(min_cc)
    else:
        print("impossible")

    min_cc = len(a)+1
    d =[0] * len(a) #初始化所有的位都是0
    dfs_2(a, d, 0) #深搜法解翻转棋子游戏
    if min_cc <= len(a):
        print(min_cc)
    else:
        print("impossible")

    

size = 4 #4*4的方阵
lib = tuple(map(lambda x: 1 << x, range(size**2-1,-1,-1)))#从高到低标记每个二进制位的1
print(lib)
min_cc = len(lib)+1
with open('fzqz.in', 'r') as fin:
    a, c = [], 0
    for line in fin.readlines():
        print(line.strip())#依次读取每行
        a.extend(line.strip()) #去掉每行头尾空白
        c += 1
        if c == 4:
            a = list(map(lambda x: x=="b", a))
            main(a)
            a, c = [], 0
    
    




