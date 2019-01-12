#!/usr/bin/python3
# 文件名: 数组基本操作之修改和交换
# 作者：巧若拙
# 时间：2018-12-17

'''
例题1.生成10个[1,100]的随机整数。
'''

'''
同步训练1.生成10个不重复的[1,100]的随机整数。
'''



'''
例题2.已知元组t存储了若干个[0,9]的随机数，请编写函数累计各个数字出现的次数。
在函数中创建并返回列表a，其中a[i]的值代表数字i出现的次数。
语法：digit_num(tuple)
参数说明：tuple -- 存储了随机数[0,9]的元组。
返回值：返回存储了各个数字出现的次数的列表。
'''
def digit_num(t):
    a = [0] * 10
    for x in t:
        a[x] += 1
    return a

'''
同步训练2.已知元组t存储了若干个正整数，请编写函数返回各元素在元组中的排名。
排名规则：数值越大排名越靠前，数值相同则排名相同。
语法：rank_1(tuple)
参数说明：tuple -- 存储了正整数的元组。
返回值：返回一个列表，其元素值为相同下标的元素在元组中的排名。
示例：对于元组a=(3,2,2,4,3,5)，返回[3,5,5,2,3,1]
'''
def rank_1_1(t): #算法1
    a = [1] * len(t)
    for i in range(0, len(t)):
        for j in range(0, len(t)):
            if t[i] < t[j]:
                a[i] += 1
    return a

def rank_1_2(t): #算法2
    a = [1] * len(t)
    for i in range(0, len(t)):
        for j in range(i+1, len(t)):
            if t[i] < t[j]:
                a[i] += 1
            elif t[i] > t[j]:
                a[j] += 1
    return a


'''
例题3.筛法求素数，生成1000以内的素数表。
'''

'''
例题4.将列表中元素反向排列。
python中用复制逆序切片list[:] = list[::-1]或者reverse() 方法实现该功能。
语法：list.reverse()
参数说明：无参数
返回值：该方法没有返回值，但是会对列表的元素进行反向排序。
我们今天编写自定义函数my_reverse()实现相同功能：
语法：my_reverse(list)
参数说明：list -- 被处理的列表。
返回值：无返回值，但是会对列表的元素进行反向排序。
'''
def my_reverse(a):
    i, j = 0, len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i, j = i + 1, j - 1

'''
同步训练4.洗牌程序。
'''

'''
课后练习1.生成斐波那契数列的前n个元素。
'''

'''
课后练习2.以较高效率求有序数组的排名，已知非递减元组t存储了若干个正整数，请编写函数返回各元素在元组中的排名。
排名规则：数值越大排名越靠前，数值相同则排名相同。
语法：rank_2(tuple)
参数说明：tuple -- 存储了正整数的非递减元组。
返回值：返回一个列表，其元素值为相同下标的元素在元组中的排名。
示例：对于元组a=(5,4,3,3,2,2)，返回[1,2,3,3,5,5]
'''
def rank_2(t):
    a = [1]
    for i in range(1, len(t)):
        if t[i] == t[i-1]:
            a.append(a[i-1])
        else:
            a.append(i+1)
    return a


'''
课后练习3.开关灯问题：有N个灯放在一排,全部处于关闭状态，从1到N依次顺序编号。
有N个人也从1到N依次编号。1号将灯全部打开, 2号将凡是2的倍数的灯关闭;
3号则对所有3的倍数的灯进行操作......一直到第n个人为止。 
那么n个人操作结束后，有几盏灯是开着的？
请编写函数模拟上述过程。
语法：light(N, n)
参数说明：N -- 共N盏灯。
          n -- 第n个人。
返回值：一个列表，存储了亮着的灯的编号。
'''
def light(N, n):
    a = [False] * (N + 1) #默认全是暗的
    for i in range(1,n+1):
        for j in range(1,N+1):
            if j % i == 0:
                a[j] = not a[j]

    b = []
    for i in range(1,N+1):
        if a[i]:
            b.append(i)
    return b

'''
课后练习4.有一组正整数，要求把奇数和偶数分成两半，
其中奇数在前，偶数在后，返回奇数的数量。
语法：odd_num(a)
参数说明：a -- 被处理的列表。
返回值：返回奇数的数量。
'''
def odd_num(a):
    i, j = 0, len(a)-1
    while i < j:
        while i < j and a[i] % 2 == 1:
            i += 1
        while i < j and a[j] % 2 == 0:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            i, j = i + 1, j - 1
    if a[i] % 2 == 1: #数组长度为奇数，且中间元素为奇数
        i += 1
    return i

'''
课后练习6.已知元组t存储了若干个正整数，请编写函数返回各元素在元组中的排名。
排名规则：数值越大排名越靠前，数值相同则比较位置，位置越靠前排名越靠前。
语法：rank_3(tuple)
参数说明：tuple -- 存储了正整数的元组。
返回值：返回一个列表，其元素值为相同下标的元素在元组中的排名。
示例：对于元组a=(3,2,2,4,3,5)，返回[3,5,6,2,4,1]
'''
def rank_3(t):
    a = [1] * len(t)
    for i in range(0, len(t)):
        for j in range(i+1, len(t)):
            if t[i] < t[j]:
                a[i] += 1
            else:
                a[j] += 1
    return a

a = (3,2,2,4,3,5)
print(a, rank_1_1(a))
print(a, rank_1_2(a))
print(a, rank_3(a))

a = (5,4,3,3,2,2)
print(a, rank_2(a))

a = [3,2,5,7,8,9,4,1]
my_reverse(a)
print(a)
p = odd_num(a)
print(p, a)

t = (2,3,4,1,2,9)
b = digit_num(t)
print(b)

c = light(10,1)
print(c)
c = light(10,2)
print(c)
c = light(10,3)
print(c)
c = light(10,4)
print(c)
