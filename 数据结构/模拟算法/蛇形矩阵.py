# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:16:52 2019

@author: Administrator
描述：输出p行q列的蛇形矩阵。
函数名：serpentine_matrix(p, q)
参数表：p--总行数;
        q--总列数
返回值:无返回值，按要求输出蛇形矩阵。
示例：p, q = 6, 5时，输出：
   1   12   13   24   25 
   2   11   14   23   26 
   3   10   15   22   27 
   4    9   16   21   28 
   5    8   17   20   29 
   6    7   18   19   30 
"""
#输出二维数组a
def show(a):
    for r in a:
        print(r)

#输出p行q列的蛇形矩阵
def serpentine_matrix(p, q):
    a = [[0 for i in range(q)] for j in range(p)]
    for i in range(p):
        for j in range(q):
            if j % 2 == 0:
                a[i][j] = j * p + i + 1
            else:
                a[i][j] = (j + 1) * p - i
    show(a)


#输出p行q列的蛇形矩阵
def serpentine_matrix_2(p, q):
    def fun(i, j):
        if j % 2 == 0:
            return j * p + i + 1
        else:
            return (j + 1) * p - i
   
    a = [list(map(fun, [i] * p, range(q))) for i in range(p)]
    show(a)
    
serpentine_matrix(6, 5)
serpentine_matrix_2(6, 5)