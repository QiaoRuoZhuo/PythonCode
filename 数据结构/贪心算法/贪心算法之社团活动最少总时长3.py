# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:08:22 2019

@author: Administrator
描述：学校筹办社团节,每个社团先到A场地做“准备”,然后到B场地“风采展示汇报"。
同一场地，同一时间只允许一个社团使用。每个社团使用A、B场地时间都有所不同。
已知学校共n个社团，第i个社团使用A场地时长为a[i]分钟,使用B场地时长为b[i]分钟。
为了更高效地组织这次活动，需要计算此次活动的最小总时长并输出社团出场的顺序。
函数名：min_time(a, b)
参数表：a--数组，存储社团i在场地A的用时
        b--数组，存储社团i在场地B的用时
返回值：活动的最小总时长，并输出社团出场的顺序和出场时刻表。
例如：社团序号为(1, 2, 3, 4, 5)，当a = (3, 5, 8, 7, 10)，b = (6, 2, 1, 4, 9)时，
返回34，并输出：
出场顺序： 1 5 4 2 3 
社团1准备时间表：0--3，表演时间表：3--9
社团5准备时间表：3--13，表演时间表：13--22
社团4准备时间表：13--20，表演时间表：22--26
社团2准备时间表：20--25，表演时间表：26--28
社团3准备时间表：25--33，表演时间表：33--34
"""
import random

def min_time(a, b):
    #m[i]表示第i个社团中在A和B两个场地中用时的较小值
    m = list(map(lambda x, y: min(x, y), a, b))
    s = range(len(a))
    ms = list(zip(m, s))
    ms.sort(key=lambda x: x[0])#按m[i]值从小到大排序
    ans = [-1] * len(a)
    k, t = 0, len(a)-1
    for i in range(len(a)):#安排社团出场顺序，准备用时少的靠前，表演用时少的靠后
        if ms[i][0] == a[ms[i][1]]:
            ans[k] = ms[i][1]
            k += 1
        else:
            ans[t] = ms[i][1]
            t -= 1
    print("出场顺序：", end=" ")
    for i in ans:#输出出场顺序
        print(i + 1, end=" ")
    print()

    ta, tb = 0, 0#分别表示社团的准备结束时刻和表演结束时刻
    for i in range(len(a)):
        print(f'社团{ans[i]+1}准备时间表：{ta}', end = "--")
        ta += a[ans[i]]#计算社团i的准备结束时刻
        #如果社团(i-1)的tb早于社团i的ta，则延长tb，使得tb=ta
        if ta > tb: 
            tb = ta
        print(f'{ta}，表演时间表：{tb}', end = "--")
        tb += b[ans[i]]#计算社团i的表演结束时刻
        print(tb)
    return tb

def min_time_2(a, b):
    def sort_ms(ms):
        low, high = 0, len(ms)
        while low < high-1:
            pmin, pmax  = -1, -1
            for i in range(low, high):
                if ms[i][0] <= ms[i][1]: #存在准备时间小于表演时间的，找准备时间最小值
                    if pmin == -1 or ms[i][0] < ms[pmin][0]:
                        pmin = i
                else:                   #否则找表演时间的最大值 
                    if pmax == -1 or ms[i][1] > ms[pmax][1]:
                        pmax = i
            if pmin != -1: #存在准备时间小于表演时间的，则准备时间短的先出场
                ms[pmin], ms[low] = ms[low], ms[pmin]
            else: #不存在准备时间小于表演时间的，则表演时间长的先出场
                ms[pmax], ms[low] = ms[low], ms[pmax]
            low += 1
            pmin, pmax = -1, -1
            for i in range(low, high):
                if ms[i][0] > ms[i][1]:#存在表演时间小于准备时间的，找表演时间最小值
                    if pmin == -1 or ms[i][1] < ms[pmin][1]:
                        pmin = i
                else:                  #否则找准备时间最大值 
                    if pmax == -1 or ms[i][0] > ms[pmax][0]:
                        pmax = i
            if pmin != -1: #存在表演时间小于准备时间的，则表演时间短的后出场
                ms[pmin], ms[high-1] = ms[high-1], ms[pmin]
            else: #不存在表演时间小于准备时间的，则准备时间长的后出场
                ms[pmax], ms[high-1] = ms[high-1], ms[pmax]
            high -= 1
            
    ms = list(zip(a, b, range(len(a))))
    sort_ms(ms)
    ans = [x[2] for x in ms]
    print("出场顺序：", end=" ")
    for i in ans:#输出出场顺序
        print(i + 1, end=" ")
    print()
    
    ta, tb = 0, 0#分别表示社团的准备结束时刻和表演结束时刻
    for i in range(len(a)):
        print(f'社团{ans[i]+1}准备时间表：{ta}', end = "--")
        ta += a[ans[i]]#计算社团i的准备结束时刻
        #如果社团(i-1)的tb早于社团i的ta，则延长tb，使得tb=ta
        if ta > tb: 
            tb = ta
        print(f'{ta}，表演时间表：{tb}', end = "--")
        tb += b[ans[i]]#计算社团i的表演结束时刻
        print(tb)
    return tb

a = (3, 5, 8, 7, 10)
b = (6, 2, 1, 4, 9)
print(f'活动总时长：{min_time(a, b)}')
print(f'活动总时长：{min_time_2(a, b)}')
