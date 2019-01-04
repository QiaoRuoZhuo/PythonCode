#!/usr/bin/python3
# 文件名: 动态规划算法之公共子序列
# 作者：巧若拙
# 时间：2019-01-02

'''
Description: 1808_公共子序列
查看 提交 统计 提问
总时间限制: 1000ms 内存限制: 65536kB
描述
我们称序列Z = < z1, z2, ..., zk >是序列X = < x1, x2, ..., xm >的子序列当且仅当存在 严格上升 的序列< i1, i2, ..., ik >，使得对j = 1, 2, ... ,k, 有xij = zj。比如Z = < a, b, f, c > 是X = < a, b, c, f, b, c >的子序列。

现在给出两个序列X和Y，你的任务是找到X和Y的最大公共子序列，也就是说要找到一个最长的序列Z，使得Z既是X的子序列也是Y的子序列。
输入
输入包括多组测试数据。每组数据包括一行，给出两个长度不超过200的字符串，表示两个序列。两个字符串之间由若干个空格隔开。
输出
对每组输入数据，输出一行，给出两个序列的最大公共子序列的长度。
样例输入
abcfbc         abfcab
programming    contest 
abcd           mnp
样例输出
4
2
0
'''
from queue import LifoQueue
        

def LCS_length_1(i, j):
    global b
    #print(b, x, y)
    if b[i][j] != 0:
        return b[i][j]
    if i == 0 or j == 0:
        b[i][j] = 0
    elif x[i-1] == y[j-1]:
        b[i][j] = LCS_length_1(i-1, j-1) + 1
    else:
        b[i][j] = max(LCS_length_1(i-1, j), LCS_length_1(i, j-1))
    return b[i][j]


def LCS_length_2(n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                b[i][j] = b[i-1][j-1] + 1
            else:
                b[i][j] = max(b[i-1][j], b[i][j-1])
    return b[n][m]


def LCS_length_3(n, m):
    pre = [0] * (m + 1) #pre[j]相当于b[i-1][j]  
    cur = [0] * (m + 1) #cur[j]相当于b[i][j] 
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                cur[j] = pre[j-1] + 1
            else:
                cur[j] = max(pre[j], cur[j-1])
        for j in range(1, m+1):
            pre[j] = cur[j]
    return cur[j]


def print_LCS_1(i, j):
    if i == 0 or j == 0:
        return
    if x[i-1] == y[j-1]:
        print_LCS_1(i-1, j-1)
        print("x[{}]={} : y[{}]={}".format(i-1,x[i-1],j-1,y[j-1]))
    elif b[i-1][j] > b[i][j-1]:
        print_LCS_1(i-1, j)
    else:
        print_LCS_1(i, j-1)

def print_LCS_2(n, m):
    s = LifoQueue()
    i, j = n, m
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            t = "x[{}]={} : y[{}]={}".format(i-1,x[i-1],j-1,y[j-1])
            s.put(t)
            i, j = i - 1, j - 1
        elif b[i-1][j] > b[i][j-1]:
            i -= 1
        else:
            j -= 1
    while not s.empty():
        print(s.get())
        

def main():
    with open('ggzxl.txt', 'r') as fin:
        for line in fin.readlines():   #依次读取每行  
            line = line.strip()      #去掉每行头尾空白
            global b
            global x
            global y
            x, y = tuple(line.split())
            b = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
            L1 = LCS_length_1(len(x), len(y))
            print(L1)
            print(x, y)
            #print(b)
            print_LCS_1(len(x), len(y))
            b = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
            L2 = LCS_length_2(len(x), len(y))
            print(L2)
            print(x, y)
            #print(b)
            print_LCS_2(len(x), len(y))
            L3 = LCS_length_3(len(x), len(y))
            print(L3)
            
x = ""
y = ""
b = []
main()
