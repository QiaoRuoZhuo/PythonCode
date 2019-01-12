#!/usr/bin/python3
# 文件名: 简单排序综合应用
# 作者：巧若拙
# 时间：2018-12-17

'''
同步训练1.有一组正整数，要求分别对奇数和偶数进行升序排序，其中奇数在前，偶数在后。
要求运用各种简单排序算法思想分别完成本题
函数名：bubble_sort_odd_even(a)
参数表：a -- 待排序列表。
返回值：该方法没有返回值，但是会对列表的对象进行排序。
'''

'''
算法分析：
选择排序：选择排序的特点是先确定最大值（最小值）将要放置的位置，再扫描待排序区域，
找到最大值（最小值）的下标，再将二者所指的元素交换位置。
现在要同时对奇数和偶数进行升序排列，只能把奇数的最小值定位在左端，
同时把偶数的最大值定位在右端，然后左右边界不断向中间移动，才能实现选择排序功能。

冒泡排序：算法分析：内层循环从右向左扫描待排序区域，
若a[j]是奇数，则将其左侧偶数和大于a[j]的奇数都交换到右侧；
否则只将其左侧大于a[j]的奇数交换到右侧。

插入排序：将当前待排序元素存储在变量t，若t是奇数，则将偶数和大于t的奇数都右移；
否则只将大于t的偶数右移。
比较直观的算法上设置变量mid指向第一个已排序偶数的下标，这样可以判断奇偶数的边界；
另一种方法是直接比较元素对2求余的结果（a[j] & 1相当于a[j] % 2），
根据余数大小可以判断二者的奇偶性。这样代码较短，但是由于求余运算过多，效率略低。
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

def bubble_sort_odd_even(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if (a[j] & 1 == a[j-1] & 1 and a[j] < a[j-1]
                or a[j] & 1 > a[j-1] & 1):
                a[j], a[j-1] = a[j-1], a[j]
                
def insert_sort_odd_even(a): #代码稍长但效率较高
    mid = 0 #mid指向第一个已排序偶数的下标
    for i in range(len(a)): #因为不知道第一个数的奇偶性，故从第1个元素开始
        t, j = a[i], i - 1
        if t & 1 == 1:  #t是奇数，则将偶数和大于t的奇数都右移
            while j >= mid or (j >= 0 and a[j] > t):
                a[j+1] = a[j]
                j -= 1
            a[j+1] = t
            mid += 1
        else:           #t是偶数，则将大于t的偶数右移
            while j >= mid and a[j] > t:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = t
            
def insert_sort_odd_even2(a): #代码简短但效率略低
    for i in range(1, len(a)):
        t, j = a[i], i - 1
        while j >= 0 and (a[j] & 1 == t & 1 and a[j] > t
                          or a[j] & 1 < t & 1):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = t

import random

a = [random.randint(1,19) for i in range(20)]
print(a)
selection_sort_odd_even(a)
print(a)
random.shuffle(a)
bubble_sort_odd_even(a)
print(a)
random.shuffle(a)
insert_sort_odd_even(a)
print(a)
random.shuffle(a)
insert_sort_odd_even2(a)
print(a)
