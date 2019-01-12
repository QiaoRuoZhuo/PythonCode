#!/usr/bin/python3
# 文件名: 数组基本操作之选择排序
# 作者：巧若拙
# 时间：2018-12-17

'''
例题1.使用选择排序算法对列表a排序。
函数名：selection_sort(a, reverse=False)
参数表：a -- 待排序列表。
        reverse -- 排序规则，reverse=True，降序；reverse=False，升序（默认）。
返回值：该方法没有返回值，但是会对列表的对象进行排序。
'''
def selection_sort(a, reverse=False): #经典选择排序算法
    if reverse:
        exp = 'a[j] > a[k]'
    else:
        exp = 'a[j] < a[k]'

    for i in range(len(a)-1):
        k = i
        for j in range(i+1, len(a)):
            if eval(exp):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]

def selection_sort2(a, reverse=False): #低效的选择排序算法
    if reverse:
        exp = 'a[j] > a[i]'
    else:
        exp = 'a[j] < a[i]'

    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if eval(exp):
                a[i], a[j] = a[j], a[i]

'''
例2、数字积木
小明有一款新式积木，每个积木上都有一个数，一天小明突发奇想，
要是把所有的积木排成一排，所形成的数目最大是多少呢?
你的任务就是读入n个数字积木，求出所能形成的最大数。
函数名：max_num(a)
参数表：a，列表，其元素为数字字符串。
返回值：返回能形成的最大整数的字符串。
示例1：a = ['13','131','343']，返回'34313131'；
示例2：a = ['23','231','243']，返回'24323231'；

算法分析：
    典型的选择排序算法。
与选择排序原型的区别在于，原型中每轮扫描是通过比较a[t]和a[j]的值，
来找到最大值的下标，而本题是通过比较拼接后字符串的大小，
即比较a[t]+a[j]和a[j]+a[t]的值，来找到能形成的最大整数的当前“最大值”的下标。
'''
def max_num(a):  #经典选择排序算法
    for i in range(len(a)-1):
        t = i
        for j in range(i+1, len(a)):
            if a[t] + a[j] < a[j] + a[t]:
                t = j
        if t != i:
            a[i], a[t] = a[t], a[i]
    return ''.join(a)

def max_num2(a): #低效的选择排序算法
    for i in range(len(a)-1):
        for j in range(i, len(a)):
            if a[i] + a[j] < a[j] + a[i]:
                a[i], a[j] = a[j], a[i]
    return ''.join(a)

'''
同步训练1.有一组正整数，要求分别对奇数和偶数进行升序排序，其中奇数在前，偶数在后。
要求运用选择排序算法思想完成本题
函数名：bubble_sort_odd_even(a)
参数表：a -- 待排序列表。
返回值：该方法没有返回值，但是会对列表的对象进行排序。

算法分析：选择排序的特点是先确定最大值（最小值）将要放置的位置，再扫描待排序区域，
找到最大值（最小值）的下标，再将二者所指的元素交换位置。
现在要同时对奇数和偶数进行升序排列，只能把奇数的最小值定位在左端，
同时把偶数的最大值定位在右端，然后左右边界不断向中间移动，才能实现选择排序功能。
'''
def selection_sort_odd_even(a):
    low, high = 0, len(a) - 1
    while low <= high:
        if a[low] & 1 == 1: #是奇数则把最小值交换到左端
            m = low
            for j in range(low+1, high+1):
                if a[j] & 1 == 1 and a[j] < a[m]:
                    m = j
            a[m], a[low] = a[low], a[m]
            low += 1 
        else: #是偶数则把最大值交换到右端
            m = low
            for j in range(low+1, high+1):
                if a[j] & 1 == 0 and a[j] > a[m]:
                    m = j
            a[m], a[high] = a[high], a[m]
            high -= 1

import random

a = [random.randint(1,9) for i in range(10)]
print(a)
selection_sort(a)
print(a)
random.shuffle(a)
print(a)
selection_sort2(a)
print(a)
random.shuffle(a)
print(a)
selection_sort(a, True)
print(a)
selection_sort_odd_even(a)
print(a)

a = ['23','231','243']
print(max_num(a))
print(max_num2(a))
