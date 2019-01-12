#!/usr/bin/python3
# 文件名: 数组基本操作之冒泡排序
# 作者：巧若拙
# 时间：2018-12-17

'''
例题1.使用冒泡排序算法对列表a排序。
函数名：bubble_sort(a, reverse=False)
参数表：a -- 待排序列表。
        reverse -- 排序规则，reverse=True，降序；reverse=False，升序（默认）。
返回值：该方法没有返回值，但是会对列表的对象进行排序。
'''
def bubble_sort(a, reverse=False):
    if reverse:
        exp = 'a[j] > a[j-1]'
    else:
        exp = 'a[j] < a[j-1]'

    for i in range(len(a)-1):
        for j in range(len(a)-1, i, -1):
            if eval(exp):
                a[j], a[j-1] = a[j-1], a[j]

'''
同步训练1.有一组正整数，要求分别对奇数和偶数进行升序排序，其中奇数在前，偶数在后。
要求运用冒泡排序算法思想完成本题
函数名：bubble_sort_odd_even(a)
参数表：a -- 待排序列表。
返回值：该方法没有返回值，但是会对列表的对象进行排序。

算法分析：内层循环从右向左扫描待排序区域，
若a[j]是奇数，则将其左侧偶数和大于a[j]的奇数都交换到右侧；
否则只将其左侧大于a[j]的奇数交换到右侧。
'''
def bubble_sort_odd_even(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if (a[j] & 1 == a[j-1] & 1 and a[j] < a[j-1]
                or a[j] & 1 > a[j-1] & 1):
                a[j], a[j-1] = a[j-1], a[j]              


import random

a = [random.randint(1,9) for i in range(10)]
print(a)
bubble_sort(a)
print(a)
random.shuffle(a)
print(a)
bubble_sort_odd_even(a)
print(a)
