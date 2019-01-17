#!/usr/bin/python3
#文件：KMP算法
#作者：巧若拙
#日期：2018年12月30日

def bf(t, p):
    i, j = 0, 0
    while i < len(t) and j < len(p):
        if t[i] == p[j]:
            i, j = i + 1, j + 1
        else:
            i, j = i - j + 1, 0
    if j == len(p):
        return i - j
    else:
        return -1

def get_failure(p): #计算失配函数值
    f = [0] * len(p)
    f[0] = -1 #/模式串p的首字符的失配函数值规定为-1
    for j in range(1, len(p)): #遍历模式串p，计算失配函数值
        k = f[j-1] #利用f[j-1]递推f[j]
        while k >= 0 and p[k] != p[j-1]: #将k回溯至p[k]==p[j-1]或k==-1
            k = f[k] 
        f[j] = k + 1 #已确保p[0…k] == p[j-k-1…j-1]或k==-1 
    return f

def get_failure2(p): #计算失配函数值：对p[j] == p[k+1]时进行修正，更高效
    f = [0] * len(p)
    f[0] = -1 #/模式串p的首字符的失配函数值规定为-1
    for j in range(1, len(p)): #遍历模式串p，计算失配函数值
        k = f[j-1] #利用f[j-1]递推f[j]，k指向f[j-1]
        while k >= 0 and p[k] != p[j-1]: #将k回溯至p[k] == p[j-1]或k == -1
            k = f[k] 
        f[j] = k + 1 #已确保p[0…k] == p[j-k-1…j-1]（若k == -1，则f[j] = 0）
    #对失配函数值进行修正，可以得到更高效的KMP算法
    for j in range(1, len(p)):  
        if p[j] == p[f[j]]: 
            f[j] = f[f[j]] 
    return f

#过早优化导致出错。当p = "AABBC"时，得不到正解
def get_failure3(p): #计算失配函数值：对p[j] == p[k+1]时进行修正，更高效
    f = [0] * len(p)
    f[0] = -1 #/模式串p的首字符的失配函数值规定为-1
    for j in range(1, len(p)): #遍历模式串p，计算失配函数值
        k = f[j-1] #利用f[j-1]递推f[j]，k指向f[j-1]
        while k >= 0 and p[k] != p[j-1]: #将k回溯至p[k] == p[j-1]或k == -1
            k = f[k] 
        f[j] = k + 1 #已确保p[0…k] == p[j-k-1…j-1]（若k == -1，则f[j] = 0）
        #过早优化导致出错。当p = "AABBC"时，得不到正解
        if p[j] == p[f[j]]: #对失配函数值进行修正，可以得到更高效的KMP算法
            f[j] = f[f[j]] 
    return f

def get_failure4(p): #计算失配函数值：有些晦涩的代码
    f = [0] * len(p)
    f[0] = -1 #/模式串p的首字符的失配函数值规定为-1
    j, k = 0, -1
    while j < len(p) - 1:
        if k == -1 or p[j] == p[k]:
            j, k = j + 1, k + 1
            if p[j] == p[k]: #当两个字符相等时要跳过
                f[j] = f[k]
            else:
                f[j] = k
        else:
            k = f[k]
    return f

            
def kmp(t, p):
    f = get_failure4(p) #先计算失配函数值
    i, j = 0, 0
    while i < len(t) and j < len(p):
        if t[i] == p[j]:
            i, j = i + 1, j + 1
        else:
            j = f[j]
            if j == -1:
                i, j = i + 1, 0
    if j == len(p):
        return i - j
    else:
        return -1

import random  
import time

a = [chr(random.randint(65, 70)) for i in range(20000)]
t = ''.join(a)
lib = []
for i in range(100):
    m = random.randint(0, 20000)
    n = random.randint(1, 20000)
    while m + n > len(t):
        n = random.randint(1, 20000)
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
    print(kmp(t, p), end=" ")
    if (kmp(t,p) == -1):
        print()
        print(p)
        print(get_failure(p))
        print(get_failure2(p))
        print(get_failure3(p))
        print(get_failure4(p))
        
t1 = time.process_time()
print()
print(t1 - t0)
