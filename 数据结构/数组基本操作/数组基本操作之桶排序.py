#!/usr/bin/python3
# 文件名: 数组基本操作之桶排序
# 作者：巧若拙
# 时间：2019-1-7


'''
同步训练1.找出字符串中第一个只出现一次的字符
函数名：first_one(s)
参数表：s -- 被访问的字符串。
返回值：返回第一个只出现一次的字符，如果不存在返回"No"。
示例: s="asdfasdfo"，返回"o"。
'''
def first_one(s):
    lib = [0] * 256
    for e in s:
        lib[ord(e)] += 1
    for e in s:
        if lib[ord(e)] == 1:
            return e
    else:
        return "No"


'''
同步训练2.根据成绩算名次。已知元组t存储了若干个学生的成绩，成绩为0到100之间的整数。
请编写函数返回各学生的名次，其中最高分为第1名，成绩相同则名次也相同。
函数名：ranking(t)
参数表：t -- 存储了学生的成绩的元组。
返回值：返回一个列表，其元素值为相同下标的元素在元组中的排名。
示例：对于元组t = (3,2,2,4,3,5)，返回[3,5,5,2,3,1]
'''
def ranking(t):
    a = [0] * 101 #存放每个分数的个数
    for i in range(len(t)): #计算每个分数的个数
        a[t[i]] += 1
    b = [0] * 101 #存放每个分数对应的名次
    mc = 1 #存放待处理分数对应的名次
    for i in range(100, -1, -1):#从高到低依次计算每个分数的排名
        if a[i] > 0: #只处理有效分数
            b[i] = mc
            mc = a[i] + b[i] #更新下一个有效分数的名次
    c = [] #存放每个学生的名次
    for i in range(len(t)): #计算每个学生的名次
        c.append(b[t[i]])
    return c


s = "asdfadfoo"
print(first_one(s))
t = (3,2,2,4,3,5)
print(ranking(t))
