# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:16:52 2019

@author: Administrator
描述：根据考生总数n，输出p行q列的考场kc的座位表，从第一位考生开始按S型依次安排座位，
每个座位号占4个字符宽度，不足4个字符的在数字前面补充空格，尾试场多余位置显示数字0。
函数名：seat_numbe(n, p, q, kc)
参数表：n--考生总数;
        p，q--考场排成p行q列;
        kc--考场序号（从1开始数起）。
返回值:无返回值，但是会按要求输出蛇形矩阵。
示例1：n, p, q, kc = 82, 6, 5, 1时，输出：
   1   12   13   24   25 
   2   11   14   23   26 
   3   10   15   22   27 
   4    9   16   21   28 
   5    8   17   20   29 
   6    7   18   19   30 
示例1：n, p, q, kc = 82, 6, 5, 3时，输出：
  61   72   73    0    0 
  62   71   74    0    0 
  63   70   75   82    0 
  64   69   76   81    0 
  65   68   77   80    0 
  66   67   78   79    0 
"""

#输出p行q列的考场kc的座位号
def seat_numbe(n, p, q, kc):
    pos = p * q * (kc - 1) + 1#本考场起始座位号
    a = [[0 for i in range(q)] for j in range(p)]
    for i in range(p):
        for j in range(q):
            if j % 2 == 0:
                a[i][j] = pos + j * p + i 
            else:
                a[i][j] = pos + (j + 1) * p - (i + 1)
            if a[i][j] > n:
                a[i][j] = 0
    for r in a: 
        for c in r:
            print(f'{c:4}', end = " ")
        print()
   

#输出p行q列的考场kc的座位号
def seat_numbe_2(n, p, q, kc):
    pos = p * q * (kc - 1) + 1#本考场起始座位号
    a = [[0 for i in range(q)] for j in range(p)]
    for j in range(q):#按照列序输出更方便
        if j % 2 == 0:
            b = range(p)
        else:
            b = range(p-1,-1,-1)
        for i in b:
            if pos <= n:
                a[i][j] = pos
                pos += 1
            else:
                break
    for r in a:
        for c in r:
            print(f'{c:4}', end = " ")
        print()

#输出p行q列的考场kc的座位号
def seat_numbe_3(n, p, q, kc): 
    def fun(i, j):
        if j % 2 == 0:
            return pos + j * p + i
        else:
            return pos + (j + 1) * p - (i + 1)

    pos = p * q * (kc - 1) + 1#本考场起始座位号
    a = [list(map(fun, [i] * q, range(q))) for i in range(p)]
    for r in a:
        for c in r:
            if c <= n:
                print(f'{c:4}', end = " ")
            else:
                print('   0', end = " ")
        print()

n = 82
p, q = 6, 5 #6行5列
for i in range(1, 4):
    seat_numbe(n, 6, 5, i)
for i in range(1, 4):
    seat_numbe_2(n, 5, 6, i)
for i in range(1, 4):
    seat_numbe_3(n, 5, 6, i)