# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:08:22 2019

@author: Administrator
学校筹办社团节,每个社团先到A场地做“准备”,然后到B场地“风采展示汇报"。
同一场地，同一时间只允许一个社团使用。每个社团使用A、B场地时间都有所不同。
已知学校共n个社团，第i个社团使用A场地时长为a[i]分钟,使用B场地时长为b[i]分钟。
为了更高效地组织这次活动，需要计算此次活动的最小总时长和社团参会的顺序。
算法思路:
1.统计m[i]表示第i个社团中在A和B两个场地中用时的较小值。
2.按m[i]值从小到大排序，然后按m[i]值的顺序，逐个社团安排参会顺序，策略如下：
为了使得总时长最短，让A场地用时最少的最先开始；B场地用时最少的最后开始。
对于每个社团，若m[i]与该社团在A场地使用时间相同，则将它排在剩余的可排位置的最前面；
若m[i]与该社团B场地使用的时间相等，则将它安排在剩余可排位置的最后面。
例如: N=5，社团序号分别是(1, 2, 3, 4, 5)
1至5号社团使用A场地的时间依次为：(3, 5, 8, 7, 10)
1至5号社团使用B场地的时间依次为：(6, 2, 1, 4, 9)
按上述算法可求得5个社团m[i]的值依次为：(3, 2, 1, 4, 9)

"""
import random

def fun1():
    #m[i]表示第i个社团中在A和B两个场地中用时的较小值
    m = list(map(lambda x, y: min(x, y), a, b))
    s = range(n)
    ms = list(zip(m, s))
    ms.sort(key=lambda x: x[0])#按m[i]值从小到大排序
    ans = [-1] * n
    k, t = 0, n-1
    for i in range(n):#安排社团出场顺序，准备用时少的靠前，表演用时少的靠后
        if ms[i][0] == a[ms[i][1]]:
            ans[k] = ms[i][1]
            k += 1
        else:
            ans[t] = ms[i][1]
            t -= 1
    '''print("出场顺序：", end=" ")
    for i in ans:#输出出场顺序
        print(i + 1, end=" ")
    print()
    '''
    ta, tb = 0, 0#分别表示社团的准备结束时刻和表演结束时刻
    for i in range(n):
        #print(f'社团{ans[i]+1}准备时间表：{ta}', end = "--")
        ta += a[ans[i]]#计算社团i的准备结束时刻
        #如果社团(i-1)的tb早于社团i的ta，则延长tb，使得tb=ta
        if ta > tb: 
            tb = ta
        #print(f'{ta}，表演时间表：{tb}', end = "--")
        tb += b[ans[i]]#计算社团i的表演结束时刻
        #print(tb)
    return tb

def fun2():
    def sort_ms(ms):
        low, high = 0, len(ms)
        while low < high-1:
            pmin, pmax  = -1, -1
            for i in range(low, high):
                if ms[i][0] <= ms[i][1]:#存在准备时间小于表演时间的，则准备时间短的先出场
                    if pmin == -1 or ms[i][0] < ms[pmin][0] or (ms[i][0] == ms[pmin][0] and ms[i][1] >= ms[pmin][1]):
                        pmin = i
                else:                 #不存在准备时间小于表演时间的，则准备时间长的先出场
                    if pmax == -1 or ms[i][1] > ms[pmax][1] or (ms[i][1] == ms[pmax][1] and ms[i][0] <= ms[pmax][0]):
                        pmax = i
            if pmin != -1: #存在准备时间小于表演时间的，则准备时间短的先出场
                ms[pmin], ms[low] = ms[low], ms[pmin]
            else: #不存在准备时间小于表演时间的，则准备时间长的先出场
                ms[pmax], ms[low] = ms[low], ms[pmax]
            low += 1
            pmin, pmax = -1, -1
            for i in range(low, high):
                if ms[i][0] > ms[i][1]:#存在表演时间小于准备时间的，则表演时间短的后出场
                    if pmin == -1 or ms[i][1] < ms[pmin][1] or (ms[i][1] == ms[pmin][1] and ms[i][0] >= ms[pmin][0]):
                        pmin = i
                else:                 #不存在表演时间小于准备时间的，则准备时间长的后出场
                    if pmax == -1 or ms[i][0] > ms[pmax][0] or (ms[i][0] == ms[pmax][0] and ms[i][1] <= ms[pmax][1]):
                        pmax = i
            if pmin != -1: #存在表演时间小于准备时间的，则表演时间短的后出场
                ms[pmin], ms[high-1] = ms[high-1], ms[pmin]
            else: #不存在表演时间小于准备时间的，则准备时间长的后出场
                ms[pmax], ms[high-1] = ms[high-1], ms[pmax]
            high -= 1
            
    ms = list(zip(a, b, range(n)))
    sort_ms(ms)
    ans = [x[2] for x in ms]
    '''print("出场顺序：", end=" ")
    for i in ans:#输出出场顺序
        print(i + 1, end=" ")
    print()
    '''
    ta, tb = 0, 0#分别表示社团的准备结束时刻和表演结束时刻
    for i in range(n):
        #print(f'社团{ans[i]+1}准备时间表：{ta}', end = "--")
        ta += a[ans[i]]#计算社团i的准备结束时刻
        #如果社团(i-1)的tb早于社团i的ta，则延长tb，使得tb=ta
        if ta > tb: 
            tb = ta
        #print(f'{ta}，表演时间表：{tb}', end = "--")
        tb += b[ans[i]]#计算社团i的表演结束时刻
        #print(tb)
    return tb

def fun21():
    def sort_ms(ms):
        low, high = 0, len(ms)
        while low < high-1:
            pmin, pmax  = -1, -1
            for i in range(low, high):
                if ms[i][0] <= ms[i][1]:#存在准备时间小于表演时间的，则准备时间短的先出场
                    if pmin == -1 or ms[i][0] < ms[pmin][0] or (ms[i][0] == ms[pmin][0] and ms[i][1] <= ms[pmin][1]):
                        pmin = i
                else:                 #不存在准备时间小于表演时间的，则准备时间长的先出场
                    if pmax == -1 or ms[i][1] > ms[pmax][1] or (ms[i][1] == ms[pmax][1] and ms[i][0] >= ms[pmax][0]):
                        pmax = i
            if pmin != -1: #存在准备时间小于表演时间的，则准备时间短的先出场
                ms[pmin], ms[low] = ms[low], ms[pmin]
            else: #不存在准备时间小于表演时间的，则准备时间长的先出场
                ms[pmax], ms[low] = ms[low], ms[pmax]
            low += 1
            pmin, pmax = -1, -1
            for i in range(low, high):
                if ms[i][0] > ms[i][1]:#存在表演时间小于准备时间的，则表演时间短的后出场
                    if pmin == -1 or ms[i][1] < ms[pmin][1] or (ms[i][1] == ms[pmin][1] and ms[i][0] >= ms[pmin][0]):
                        pmin = i
                else:                 #不存在表演时间小于准备时间的，则准备时间长的后出场
                    if pmax == -1 or ms[i][0] > ms[pmax][0] or (ms[i][0] == ms[pmax][0] and ms[i][1] <= ms[pmax][1]):
                        pmax = i
            if pmin != -1: #存在表演时间小于准备时间的，则表演时间短的后出场
                ms[pmin], ms[high-1] = ms[high-1], ms[pmin]
            else: #不存在表演时间小于准备时间的，则准备时间长的后出场
                ms[pmax], ms[high-1] = ms[high-1], ms[pmax]
            high -= 1
            
    ms = list(zip(a, b, range(n)))
    sort_ms(ms)
    ans = [x[2] for x in ms]
    '''print("出场顺序：", end=" ")
    for i in ans:#输出出场顺序
        print(i + 1, end=" ")
    print()
    '''
    ta, tb = 0, 0#分别表示社团的准备结束时刻和表演结束时刻
    for i in range(n):
        #print(f'社团{ans[i]+1}准备时间表：{ta}', end = "--")
        ta += a[ans[i]]#计算社团i的准备结束时刻
        #如果社团(i-1)的tb早于社团i的ta，则延长tb，使得tb=ta
        if ta > tb: 
            tb = ta
        #print(f'{ta}，表演时间表：{tb}', end = "--")
        tb += b[ans[i]]#计算社团i的表演结束时刻
        #print(tb)
    return tb

def fun22():
    def sort_ms(ms):
        low, high = 0, len(ms)
        while low < high-1:
            pmin, pmax  = -1, -1
            for i in range(low, high):
                if ms[i][0] <= ms[i][1]:#存在准备时间小于表演时间的，则准备时间短的先出场
                    if pmin == -1 or ms[i][0] < ms[pmin][0] or (ms[i][0] == ms[pmin][0] and ms[i][1] >= ms[pmin][1]):
                        pmin = i
                else:                 #不存在准备时间小于表演时间的，则准备时间长的先出场
                    if pmax == -1 or ms[i][1] > ms[pmax][1] or (ms[i][1] == ms[pmax][1] and ms[i][0] <= ms[pmax][0]):
                        pmax = i
            if pmin != -1: #存在准备时间小于表演时间的，则准备时间短的先出场
                ms[pmin], ms[low] = ms[low], ms[pmin]
            else: #不存在准备时间小于表演时间的，则准备时间长的先出场
                ms[pmax], ms[low] = ms[low], ms[pmax]
            low += 1
            pmin, pmax = -1, -1
            for i in range(low, high):
                if ms[i][0] > ms[i][1]:#存在表演时间小于准备时间的，则表演时间短的后出场
                    if pmin == -1 or ms[i][1] < ms[pmin][1] or (ms[i][1] == ms[pmin][1] and ms[i][0] <= ms[pmin][0]):
                        pmin = i
                else:                 #不存在表演时间小于准备时间的，则准备时间长的后出场
                    if pmax == -1 or ms[i][0] > ms[pmax][0] or (ms[i][0] == ms[pmax][0] and ms[i][1] >= ms[pmax][1]):
                        pmax = i
            if pmin != -1: #存在表演时间小于准备时间的，则表演时间短的后出场
                ms[pmin], ms[high-1] = ms[high-1], ms[pmin]
            else: #不存在表演时间小于准备时间的，则准备时间长的后出场
                ms[pmax], ms[high-1] = ms[high-1], ms[pmax]
            high -= 1
            
    ms = list(zip(a, b, range(n)))
    sort_ms(ms)
    ans = [x[2] for x in ms]
    '''print("出场顺序：", end=" ")
    for i in ans:#输出出场顺序
        print(i + 1, end=" ")
    print()
    '''
    ta, tb = 0, 0#分别表示社团的准备结束时刻和表演结束时刻
    for i in range(n):
        #print(f'社团{ans[i]+1}准备时间表：{ta}', end = "--")
        ta += a[ans[i]]#计算社团i的准备结束时刻
        #如果社团(i-1)的tb早于社团i的ta，则延长tb，使得tb=ta
        if ta > tb: 
            tb = ta
        #print(f'{ta}，表演时间表：{tb}', end = "--")
        tb += b[ans[i]]#计算社团i的表演结束时刻
        #print(tb)
    return tb

def fun23():
    def sort_ms(ms):
        low, high = 0, len(ms)
        while low < high-1:
            pmin, pmax  = -1, -1
            for i in range(low, high):
                if ms[i][0] <= ms[i][1]:#存在准备时间小于表演时间的，则准备时间短的先出场
                    if pmin == -1 or ms[i][0] < ms[pmin][0] or (ms[i][0] == ms[pmin][0] and ms[i][1] <= ms[pmin][1]):
                        pmin = i
                else:                 #不存在准备时间小于表演时间的，则准备时间长的先出场
                    if pmax == -1 or ms[i][1] > ms[pmax][1] or (ms[i][1] == ms[pmax][1] and ms[i][0] <= ms[pmax][0]):
                        pmax = i
            if pmin != -1: #存在准备时间小于表演时间的，则准备时间短的先出场
                ms[pmin], ms[low] = ms[low], ms[pmin]
            else: #不存在准备时间小于表演时间的，则准备时间长的先出场
                ms[pmax], ms[low] = ms[low], ms[pmax]
            low += 1
            pmin, pmax = -1, -1
            for i in range(low, high):
                if ms[i][0] > ms[i][1]:#存在表演时间小于准备时间的，则表演时间短的后出场
                    if pmin == -1 or ms[i][1] < ms[pmin][1] or (ms[i][1] == ms[pmin][1] and ms[i][0] >= ms[pmin][0]):
                        pmin = i
                else:                 #不存在表演时间小于准备时间的，则准备时间长的后出场
                    if pmax == -1 or ms[i][0] > ms[pmax][0] or (ms[i][0] == ms[pmax][0] and ms[i][1] >= ms[pmax][1]):
                        pmax = i
            if pmin != -1: #存在表演时间小于准备时间的，则表演时间短的后出场
                ms[pmin], ms[high-1] = ms[high-1], ms[pmin]
            else: #不存在表演时间小于准备时间的，则准备时间长的后出场
                ms[pmax], ms[high-1] = ms[high-1], ms[pmax]
            high -= 1
            
    ms = list(zip(a, b, range(n)))
    sort_ms(ms)
    ans = [x[2] for x in ms]
    '''print("出场顺序：", end=" ")
    for i in ans:#输出出场顺序
        print(i + 1, end=" ")
    print()
    '''
    ta, tb = 0, 0#分别表示社团的准备结束时刻和表演结束时刻
    for i in range(n):
        #print(f'社团{ans[i]+1}准备时间表：{ta}', end = "--")
        ta += a[ans[i]]#计算社团i的准备结束时刻
        #如果社团(i-1)的tb早于社团i的ta，则延长tb，使得tb=ta
        if ta > tb: 
            tb = ta
        #print(f'{ta}，表演时间表：{tb}', end = "--")
        tb += b[ans[i]]#计算社团i的表演结束时刻
        #print(tb)
    return tb

def fun3():
    def sort_ms(ms):
        low, high = 0, len(ms)
        while low < high-1:
            pmin, pmax  = -1, -1
            for i in range(low, high):
                if ms[i][0] <= ms[i][1]:#存在准备时间小于表演时间的，则准备时间短的先出场
                    if pmin == -1 or ms[i][0] < ms[pmin][0]:
                        pmin = i
                else:                 #不存在准备时间小于表演时间的，则准备时间长的先出场
                    if pmax == -1 or ms[i][1] > ms[pmax][1]:
                        pmax = i
            if pmin != -1: #存在准备时间小于表演时间的，则准备时间短的先出场
                ms[pmin], ms[low] = ms[low], ms[pmin]
            else: #不存在准备时间小于表演时间的，则准备时间长的先出场
                ms[pmax], ms[low] = ms[low], ms[pmax]
            low += 1
            pmin, pmax = -1, -1
            for i in range(low, high):
                if ms[i][0] > ms[i][1]:#存在表演时间小于准备时间的，则表演时间短的后出场
                    if pmin == -1 or ms[i][1] < ms[pmin][1]:
                        pmin = i
                else:                 #不存在表演时间小于准备时间的，则准备时间长的后出场
                    if pmax == -1 or ms[i][0] > ms[pmax][0]:
                        pmax = i
            if pmin != -1: #存在表演时间小于准备时间的，则表演时间短的后出场
                ms[pmin], ms[high-1] = ms[high-1], ms[pmin]
            else: #不存在表演时间小于准备时间的，则准备时间长的后出场
                ms[pmax], ms[high-1] = ms[high-1], ms[pmax]
            high -= 1
            
    ms = list(zip(a, b, range(n)))
    sort_ms(ms)
    ans = [x[2] for x in ms]
    '''print("出场顺序：", end=" ")
    for i in ans:#输出出场顺序
        print(i + 1, end=" ")
    print()
    '''
    ta, tb = 0, 0#分别表示社团的准备结束时刻和表演结束时刻
    for i in range(n):
        #print(f'社团{ans[i]+1}准备时间表：{ta}', end = "--")
        ta += a[ans[i]]#计算社团i的准备结束时刻
        #如果社团(i-1)的tb早于社团i的ta，则延长tb，使得tb=ta
        if ta > tb: 
            tb = ta
        #print(f'{ta}，表演时间表：{tb}', end = "--")
        tb += b[ans[i]]#计算社团i的表演结束时刻
        #print(tb)
    return tb


n = 5
a = (3,5,8,7,10)
b = (6,2,1,4,9)
a = (3 , 3 , 3 , 6 , 6)
b = (4 , 5 , 1 , 3 , 4)
for i in range(2000):
    n = random.randint(3, 50)
    a = [random.randint(1, 10) for j in range(n)]
    b = [random.randint(1, 10) for j in range(n)]
    f1 = fun1()
    f2 = fun2()
    f3 = fun3()
    f21 = fun21()
    f22 = fun22()
    f23 = fun23()
    if f1 == f2 == f3 == f21 == f22 == f23:
        print("ok", end=" ")
    else:
        print(f1, f2, f3, f21, f22, f23,a, b)
