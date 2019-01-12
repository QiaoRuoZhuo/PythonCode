#!/usr/bin/python3
# 文件名: 数组基本操作之插入排序
# 作者：巧若拙
# 时间：2018-12-17

'''
例题1.使用插入排序算法对列表a排序。
函数名：bubble_sort(a, reverse=False)
参数表：a -- 待排序列表。
        reverse -- 排序规则，reverse=True，降序；reverse=False，升序（默认）。
返回值：该方法没有返回值，但是会对列表的对象进行排序。
'''
def insert_sort(a, reverse=False):
    if reverse:
        exp = 'j >= 0 and a[j] < t'
    else:
        exp = 'j >= 0 and a[j] > t'

    for i in range(1, len(a)):
        t, j = a[i], i - 1
        while eval(exp):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = t

'''
同步训练1.有一组正整数，要求分别对奇数和偶数进行升序排序，其中奇数在前，偶数在后。
要求运用插入排序算法思想完成本题
函数名：bubble_sort_odd_even(a)
参数表：a -- 待排序列表。
返回值：该方法没有返回值，但是会对列表的对象进行排序。

算法分析：将当前待排序元素存储在变量t，若t是奇数，则将偶数和大于t的奇数都右移；
否则只将大于t的偶数右移
比较直观的算法上设置变量mid指向第一个已排序偶数的下标，这样可以判断奇偶数的边界；
另一种方法是直接比较元素对2求余的结果（a[j] & 1相当于a[j] % 2），
根据余数大小可以判断二者的奇偶性。这样代码较短，但是由于求余运算过多，效率略低。
'''
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
insert_sort(a)
print(a)
random.shuffle(a)
insert_sort_odd_even(a)
print(a)
random.shuffle(a)
insert_sort_odd_even2(a)
print(a)
