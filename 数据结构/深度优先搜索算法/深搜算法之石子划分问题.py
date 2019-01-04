#!/usr/bin/python3
#文件：深搜算法之石子划分问题
#作者：巧若拙
#日期：2019年1月4日
'''
给出n堆石子，以及每堆石子数。请将它们分为两堆，使得这两堆的总石子数差最小。
输入n，以及每堆石子数，输出分为两堆后的最小差值。
比如，n＝4，四堆石子分别有13，6，8，14颗，则可以分为13＋8和14＋6的两堆，它们的最小差为1。
分堆算法为
（1）求得所有石子数total，以及它的一半half；
（2）在所有石子堆中作适当选择，对每种选择方案，求不超过half的己选中堆中的石子总数的最大值mx。
所求即为（total－max）－max。
（3）以a(j)表示第j堆石子数；以b(j)表示第j堆石子是否被选中，
如果b(j)＝1，表示第j堆被选中，如果b(j)＝0表示第j堆没有被选中。
（4）各种方案的表达及次序如下：
以00…00（均不选中），00…01（只选中第n堆石子），00…10（只选中第n－1堆石子），
00…11（选中第n－1堆和第n堆石子），00…100（选中第n－2堆石子），
00…101（选中第n－2堆和第n堆石子），11…11（选中所有n堆石子）。

算法分析：
本题算法思想与“广搜算法之翻转棋子游戏”如出一辙。
初看本题，最容易想到的是穷举法，用包含n个元素的列表b分别表示堆石子的选择状态，b[i]=1表示选择第i堆石子，b[i]=0表示不选择。
可以穷举从b=[0,0,...0,0]到b=[1,1,...1,1]，即从都不选择到都选择。
若把列表b的值对应整数t的n位二进制数，则相当于穷举从t=0到t=2^n-1。
比较直白的算法是循环遍历每一个t，将t的n位二进制数存储到列表b；然后遍历b，若b[i]=1则选择第i堆石子；
完成本选择模式后，判断是否有解，若本选择模式能获得更好的解，则更新最优解。
上述算法思想简单明了，但把整数t转化成二进制数并存储到列表b的操作比较耗费时间。
我们可以使用位运算来处理整数t的二进制数，这样就无需引入列表b，可以直接操作整数t了，效率有所提升。
穷举法是容易想到的算法，但是效率实在太低，我们可以使用深度优先搜索（回溯加剪枝）来实现同样的功能。
这样我们就分别用穷举和深搜两种算法实现了所需功能。
回到最初的想法，我们使用列表b来表示整数t的二进制数的每一位，是很直观的想法，只不过每次都需要把整数转化成二进制数比较耗费时间；
其实我们可以直接修改列表b的值来模拟整数t递增的过程，这样就不需要引入整数t及其位运算了，数据结构更清晰。
我也用这种数据结构实现了穷举和深搜两种算法。
'''

#将整数t的n位二进制数存储到列表d
def binary_number(t, n): 
    d =[0] * n #高位补零，凑足n位
    i = n -1
    while t > 0:
        d[i] = t & 1         #相当于t % 2
        i, t = i - 1, t >> 1 #相当于t // 2
    return d

#穷举法解石子划分问题：最直观的想法，把整数t的n位二进制数存储到列表b，并根据列表b的值来确定选择模式
def divide_stones_0(a):
    n, max_s = len(a), 0
    for t in range(1<<n): #遍历从[0,1<<len(a)]的所有选择模式
        b = binary_number(t, n) #将整数t的n位二进制数存储到列表b
        s = 0
        for i in range(n):
            s += a[i] * b[i] #累计被选中的石子堆的数量
        if s > max_s and s <= half: #更新最优解
            max_s = s
            d = b.copy()  
    s1, s2 = 0, 0
    for i in range(len(d)):
        if d[i] == 0:
            s1 += a[i]
        else:
            s2 += a[i]
    print(s1, s2, d)
    return total - max_s * 2 #返回最小差值

#穷举法解石子划分问题：直接用位运算操作整数t的各个二进制数位，效率更高
def divide_stones_1(a):
    n, max_s = len(a), 0
    lib = tuple(map(lambda x: 1 << x, range(n-1,-1,-1)))#从高到低标记每个二进制位的1
    for t in range(1<<n): #遍历从[0,1<<len(a)]的所有选择模式
        s = 0
        for i in range(n):
            if t & lib[i] > 0: #t的二进制数第i位是1，则选择该堆石子 
                s += a[i]      #累计被选中的石子堆的数量
        if s > max_s and s <= half: #更新最优解
            max_s = s
            ans = t
    fun = lambda i: int(ans & lib[i] > 0)
    d = list(map(fun, range(n)))
    s1, s2 = 0, 0
    for i in range(len(d)):
        if d[i] == 0:
            s1 += a[i]
        else:
            s2 += a[i]
    print(s1, s2, d)
    return total - max_s * 2 #返回最小差值

#穷举法解石子划分问题：直接修改列表b的值来模拟整数t递增的过程，无需进行位运算，更好理解
def divide_stones_2(a):
    n, max_s = len(a), 0
    b =[0] * n #初始化所有的位都是0
    i = n - 1  #先选择第n堆
    while i >= 0: #遍历从[0,1<<len(a)]的所有选择模式
        s, b[i] = 0, 1       #将b[i]右侧的1都改成0，b[i]改成1，相当于二进制数递增1
        for i in range(len(b)):
            s += a[i] * b[i] #累计被选中的石子堆的数量
        if s > max_s and s <= half: #更新最优解
            max_s = s
            d = b.copy()
        i = n - 1
        while i >= 0 and b[i] == 1: #修改列表b的值来模拟整数t递增的过程，每次递增1
            b[i] = 0         
            i -= 1        #当b[i]==0时跳出循环，并将b[i]改成1，相当于二进制数递增1
    s1, s2 = 0, 0
    for i in range(len(d)):
        if d[i] == 0:
            s1 += a[i]
        else:
            s2 += a[i]
    print(s1, s2, d)
    return total - max_s * 2 #返回最小差值


#深搜法解石子划分问题：直接用位运算操作整数t的各个二进制数位，每层递归函数的选择模式都继承自上一层函数，每层只选择1堆石子
#参数介绍：a——列表，存储各堆石子数量；t——正整数，其二进制数代表当前选择模式；s——正整数，表示已经选择的石子数量。
def dfs_1(a, t, s):
    global max_s
    global ans
    if s > max_s: #更新最优解
        max_s, ans = s, t
    for i in range(len(lib)):
        if t & lib[i] == 0:     #只在第一个值为1的二进制位左侧设置1，以避免重复
            if s+a[i] <= half:  #已经超出半数就无需再选择新的石子堆了
                t |= lib[i]     #将整数t的第i个二进制位设置成1
                dfs_1(a, t, s+a[i])
                t &= ~lib[i]    #将整数t的第i个二进制位恢复成0
        else:
            break

#深搜法解石子划分问题：使用列表b存储当前翻转模式，每层递归函数的选择模式都继承自上一层函数，每层只选择1堆石子
#参数介绍：a——列表，存储各堆石子数量；b——列表，存储当前选择模式；s——正整数，表示已经选择的石子数量。
def dfs_2(a, b, s):
    global max_s
    global ans
    if s > max_s: #更新最优解
        max_s, ans = s, b.copy()
    for i in range(len(b)):
        if b[i] == 0:     #只在第一个值为1的二进制位左侧设置1，以避免重复
            if s+a[i] <= half:  #已经超出半数就无需再选择新的石子堆了
                b[i] = 1    #将整数t的第i个二进制位设置成1
                dfs_2(a, b, s+a[i])
                b[i] = 0     #将整数t的第i个二进制位恢复成0
        else:
            break
           

with open('szhf.txt', 'r') as fin:
    for line in fin.readlines():
        print(line.strip())#依次读取每行
        a = list(map(int, line.strip().split(",")))
        total = sum(a)
        half = total / 2
        print(divide_stones_0(a))
        print(divide_stones_1(a))
        print(divide_stones_2(a))
        
        max_s, ans = 0, 0
        lib = tuple(map(lambda x: 1 << x, range(len(a)-1,-1,-1)))#从高到低标记每个二进制位的1
        dfs_1(a, 0, 0)
        fun = lambda i: int(ans & lib[i] > 0)
        d = list(map(fun, range(len(a))))
        print(d)
        print(total - max_s * 2)

        b =[0] * len(a) #初始化所有的位都是0
        max_s, ans = 0, b.copy()
        dfs_2(a, b, 0)
        print(ans)
        print(total - max_s * 2)
