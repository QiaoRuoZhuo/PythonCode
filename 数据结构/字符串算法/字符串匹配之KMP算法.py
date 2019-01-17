#!/usr/bin/python3
#文件：生成翻转棋子游戏数据
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
    print(f)   
    return f

def get_failure2(p): #计算失配函数值：对p[j] == p[k+1]时进行修正，更高效
    f = [0] * len(p)
    f[0] = -1 #/模式串p的首字符的失配函数值规定为-1
    for j in range(1, len(p)): #遍历模式串p，计算失配函数值
        k = f[j-1] #利用f[j-1]递推f[j]，k指向f[j-1]
        while k >= 0 and p[k] != p[j-1]: #将k回溯至p[k] == p[j-1]或k == -1
            k = f[k] 
        f[j] = k + 1 #已确保p[0…k] == p[j-k-1…j-1]（若k == -1，则f[j] = 0）
        if p[j] == p[k+1]: #对失配函数值进行修正，可以得到更高效的KMp算法
            f[j] = f[k+1]
    print(f)   
    return f

def get_failure3(p): #计算失配函数值：有些晦涩的代码
    f = [0] * len(p)
    f[0] = -1 #/模式串p的首字符的失配函数值规定为-1
    k = 0
    for j in range(1, len(p)): #遍历模式串p，计算失配函数值
        if p[j] == p[k]: #对失配函数值进行修正，可以得到更高效的KMp算法
            f[j] = f[k]
        else:
            f[j] = k
            while k >= 0 and p[k] != p[j]: #将k回溯至p[k] == p[j]或k == -1
                k = f[k] 
            k += 1 
    print(f)      
    return f
            
def kmp(t, p):
    f = get_failure(p) #先计算失配函数值
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

t = "aabaabaabaabc"
p = "abcaabcab"
get_failure(p)
get_failure2(p)
print(bf(t, p))
print(kmp(t, p))
        
