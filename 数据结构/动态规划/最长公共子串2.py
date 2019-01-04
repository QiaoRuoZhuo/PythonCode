#!/usr/bin/python3
# 文件名: 动态规划算法之最长公共子串
# 作者：巧若拙
# 时间：2019-01-04

'''
两个字符串的最长公共子串与最长公共子序列的区别：
最长公共子串要求在原字符串中是连续的，
而子序列只需要保持相对顺序一致，并不要求连续。
'''

#算法1：最直接的暴力穷举，需要三重循环，效率较低
def LSS_length_1(n, m):
#最大长度和子串的末端索引（按照左闭右开原则，实际上该索引对应的元素取不到）
    max_len, end_pos = 0, 0 
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                c, min_len = 1, min(n - i, m - j)
                while c < min_len and x[i+c] == y[j+c]: #统计连续子串长度
                    c += 1   
                if max_len < c:  #更新最大长度和子串的末端索引
                    max_len, end_pos = c, j + c
    return (max_len, end_pos)

#算法2：x不动，y从左向右逐个移动比较，移动n+m步，只需二重循环，效率有所提高
def LSS_length_2(n, m):
#最大长度和子串的末端索引（按照左闭右开原则，实际上该索引对应的元素取不到）
    max_len, end_pos = 0, 0
    for i in range(1, n+m):
        start_x, start_y = max(i-m, 0), max(m-i, 0) #x和y的起始比较位置
        cover_len = i - start_x - max(i-n, 0) #字符串重叠部分长度
        c = 0 
        for j in range(cover_len): #遍历重叠部分
            if x[start_x+j] == y[start_y+j]: #统计连续子串长度
                c += 1  
            else:    
                if max_len < c:  #更新最大长度和子串的末端索引
                    max_len, end_pos = c, start_y+j
                c = 0
    return (max_len, end_pos)

#算法3：动态规划，使用一个二维列表来存储中间值
def LSS_length_3(n, m):
#最大长度和子串的末端索引（按照左闭右开原则，实际上该索引对应的元素取不到）
    max_len, end_pos = 0, 0
    b = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                b[i][j] = b[i-1][j-1] + 1
                if max_len < b[i][j]: #更新最大长度和子串的末端索引
                    max_len, end_pos = b[i][j], j
            else:
                b[i][j] = 0
    return (max_len, end_pos)

#算法4：对LSS_length_3()进行降维优化，使用2个一维列表来存储中间值
def LSS_length_4(n, m):
#最大长度和子串的末端索引（按照左闭右开原则，实际上该索引对应的元素取不到）
    max_len, end_pos = 0, 0
    pre = [0] * (m + 1) #pre[j]相当于b[i-1][j]  
    cur = [0] * (m + 1) #cur[j]相当于b[i][j]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                cur[j] = pre[j-1] + 1
                if max_len < cur[j]: #更新最大长度和子串的末端索引
                    max_len, end_pos = cur[j], j
            else:
                cur[j] = 0
        for j in range(1, m+1):
            pre[j] = cur[j]
    return (max_len, end_pos)

with open('zcggzc.txt', 'r') as fin:
    for line in fin.readlines():   #依次读取每行  
        line = line.strip()      #去掉每行头尾空白
        x, y = tuple(line.split())
        print(x, y)
        max_len, end_pos = LSS_length_1(len(x), len(y))
        print("最大公共子串为：{} 其长度是：{}"
              .format(y[end_pos-max_len:end_pos],max_len))

        max_len, end_pos = LSS_length_2(len(x), len(y))
        print("最大公共子串为：{} 其长度是：{}"
              .format(y[end_pos-max_len:end_pos],max_len))

        max_len, end_pos = LSS_length_3(len(x), len(y))
        print("最大公共子串为：{} 其长度是：{}"
              .format(y[end_pos-max_len:end_pos],max_len))

        max_len, end_pos = LSS_length_4(len(x), len(y))
        print("最大公共子串为：{} 其长度是：{}"
              .format(y[end_pos-max_len:end_pos],max_len))

