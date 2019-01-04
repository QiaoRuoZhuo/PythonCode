#!/usr/bin/python3
#文件：生成石子划分问题数据
#作者：巧若拙
#日期：2019年1月4日

from random import randint

with open('szhf.txt', 'w') as fout:
    for i in range(8):
        n = randint(2, 20)
        a = []
        for j in range(n):
            a.append(randint(1, 50))
        c = ",".join(list(map(str, a)))#生成各堆石子的数量
        print(c)
        fout.writelines(c + "\n")


