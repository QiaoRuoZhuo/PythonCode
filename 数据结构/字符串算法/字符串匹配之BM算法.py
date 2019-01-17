#!/usr/bin/python3
# 文件名: 字符串匹配之BM算法
# 作者：巧若拙
# 时间：2019-1-15

def bf(t, p):
    for left in range(len(t)-len(p)+1): #left指向当前t和p的左边界对齐的位置
        j = len(p) - 1              #j指向当前比较的位置
        while j >= 0:
            if p[j] == t[left+j]: #从右向左依次匹配
                j -= 1
            else:
                break
        else:
            return left
    else:     
        return -1

def get_badchar(p): #计算坏字符规则字典
    bc = {}
    for k, i in zip(p, range(len(p))):
        bc[k] = i
    return bc


#前缀表：suf[i]表示以i为右边界，与模式串后缀匹配的最大长度
def suffixes(p):
    n = len(p)
    suf = [0] * n
    suf[n-1] = n
    for i in range(n-2, -1, -1):
        s = 0
        while s <= i and p[i-s] == p[n-1-s]:
            s += 1
        suf[i] = s #满足p[i-s, i]==p[n-1-s, n-1]的最大长度s。
    return suf

'''
为了防止回溯，我们应该尽量让一次移动的距离少一点。
优先匹配串中子串，其次是最大前缀，最后再是移动整个模式串。
'''
def get_good_suffix(p):
    n = len(p)
    gs = [n] * n #初始化移动距离均为n
    suf = suffixes(p) #生成前缀表
    #有前缀的，按照从大到小的顺序设置好前缀移动距离，这样无需覆盖，效率更高
    for i in range(n-2, -1, -1):
        if suf[i] == i + 1: #可能存在多个前缀
            j = n - 2 - i
            while j >= 0 and gs[j] == n: #只更新那些没有更新过的元素
                gs[j] = n - 1 - i
                j -= 1
    for i in range(n-1): #更新匹配子串的移动距离
        gs[n-1-suf[i]] = n - 1 - i
    return gs

#算法1：从左向右寻找“前缀”，越晚出现的“前缀”越长
def get_good_suffix_1(p):
    n = len(p)
    gs = [n] * n #初始化移动距离均为n
    suf = suffixes(p) #生成前缀表
    #有前缀的，按照从小到大的顺序更新前缀的移动距离
    for i in range(n-1): 
        if suf[i] == i + 1: #可能存在多个前缀，用长的覆盖短的
            for j in range(n-1-i): #更新前缀的移动距离
                gs[j] = n - 1 - i
    for i in range(n-1): #更新匹配子串的移动距离
        gs[n-1-suf[i]] = n - 1 - i
    return gs


#一个可用，但效率较低的版本，低效的原因是对所有已更新元素都进行了判断
def get_good_suffix_3(p):
    n = len(p)
    gs = [n] * n #初始化移动距离均为n，即找不到匹配子串和前缀
    suf = suffixes(p) #生成前缀表
    #有前缀的，按照从大到小的顺序设置好前缀移动距离
    for i in range(n-1, -1, -1):
        if suf[i] == i + 1: #存在我们想要的前缀
            for j in range(n-1-i):
                if gs[j] == n: #其实一旦遇到已更新元素就应该跳出循环
                    gs[j] = n - 1 - i
    for i in range(n-1): #更新匹配子串的移动距离
        gs[n-1-suf[i]] = n - 1 - i
    return gs
'''
#一个具有迷惑性的错误版本：只处理最大前缀，不处理短前缀，导致出错
def get_good_suffix3(p):
    n = len(p)
    gs = [n] * n #初始化移动距离均为n，即找不到匹配子串和前缀
    suf = suffixes(p) #生成前缀表
    i = n - 2
    while i >= 0 and suf[i] != i + 1:
        i -= 1
    if suf[i] == i + 1: #存在最大前缀
        for j in range(n-1-i):
            gs[j] = n - 1 - i
    for i in range(n-1): #更新匹配子串的移动距离
        gs[n-1-suf[i]] = n - 1 - i
    return gs
'''



def bm(t, p):
    bc = get_badchar(p)  #计算坏字符规则字典
    gs = get_good_suffix(p)#计算好后缀列表
    len_p, len_t = len(p), len(t)
    left = 0
    while left + len_p <= len_t:
        j = len_p - 1
        while j >= 0:
            if p[j] == t[left+j]: #从右向左依次匹配
                j -= 1
            else:
                span = j - bc.get(t[left+j], -1) #返回对应坏字符跳过的距离
                #left += max(span, 1) #如果坏字符出现在j右侧，则前进1步
                left += max(span, gs[j]) #从坏字符字典和好后缀列表中取较大值
                break
        else:
            return left
    else:     
        return -1


import random  
import time

a = [chr(random.randint(65, 70)) for i in range(200000)]
t = ''.join(a)
lib = []
for i in range(100):
    m = random.randint(0, 200000)
    n = random.randint(1, 200000)
    while m + n > len(t):
        n = random.randint(1, 200000)
    lib.append((m, m+n))
#print(lib)
t0 = time.process_time() 
for x in lib:
    p = t[x[0]:x[1]]
    print(t.find(p), end=" ")
t1 = time.process_time()
print()
print(t1 - t0)

t0 = time.process_time()
for x in lib:
    p = t[x[0]:x[1]]
    print(bm(t, p), end=" ")
t1 = time.process_time()
print()
print(t1 - t0)
'''
a = [chr(random.randint(65, 70)) for i in range(200)]
t = ''.join(a)
print(t)
for i in range(10):
    m = random.randint(0, 200)
    p = t[m:]
    print(t.find(p), bf(t, p), bm(t, p))
p = "abcabcab"
suf = suffixes(p) #生成前缀表
print(suf)
gs = get_good_suffix(p)#计算好后缀列表
print(gs)
gs = get_good_suffix2(p)#计算好后缀列表
print(gs)
print(t.find(p))
print(bf(t, p))
bc = get_badchar(p)  #计算坏字符hash字典
print(bc)
print(bm(t, p))
'''
