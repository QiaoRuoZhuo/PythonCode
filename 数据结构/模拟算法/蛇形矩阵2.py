# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:16:52 2019

@author: Administrator
描述：输出p行q列的蛇形矩阵。
函数名：serpentine_matrix(p, q)
参数表：p--总行数;
        q--总列数
返回值:无返回值，按要求输出蛇形矩阵。
示例1：p, q = 6, 5时，输出：
   1   12   13   24   25 
   2   11   14   23   26 
   3   10   15   22   27 
   4    9   16   21   28 
   5    8   17   20   29 
   6    7   18   19   30 
示例1：p, q = 5, 6时，输出：
   1    2    3    4    5    6 
  12   11   10    9    8    7 
  13   14   15   16   17   18 
  24   23   22   21   20   19 
  25   26   27   28   29   30 
"""
#输出p行q列的蛇形矩阵
def serpentine_matrix(p, q):
    pos = 1
    a = [[0 for i in range(q)] for j in range(p)]
    for i in range(p):
        if i % 2 == 0:
            b = range(q)
        else:
            b = range(q-1,-1,-1)
        for j in b:
            a[i][j] = pos
            pos += 1
    for r in a:
        for c in r:
            print(f'{c:4}', end = " ")
        print()


#输出p行q列的蛇形矩阵
def serpentine_matrix_2(p, q):
    def fun(i, j):
        if i % 2 == 0:
            return i * q + j + 1
        else:
            return (i + 1) * q - j
   
    a = [list(map(fun, [i] * q, range(q))) for i in range(p)]
    for r in a:
        for c in r:
            print(f'{c:4}', end = " ")
        print()
    
serpentine_matrix(6, 5)
serpentine_matrix_2(5, 6)