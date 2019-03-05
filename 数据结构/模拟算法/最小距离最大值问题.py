#!/usr/bin/python3
# 文件名: 最小距离最大值问题
# 作者：巧若拙
# 时间：2019-01-23
'''
最小距离最大值问题。
描述：元组a是一个递增正整数序列（其中a[0]=0），
求从a[1:]中删除m个元素以后，剩下的元素中最小距离的最大值。
距离是指当前元素减去前一个元素的差。
函数名：distance(a, m)
参数表：a，存储了递增正整数序列的元组
        m，删除的元素个数
返回值：返回剩下的元素中最小距离的最大值
例如：当a = (0,2,11,14,17,21,25)，m = 2时，返回4。
分析过程：如果删除元素“2”和“11”，剩下的元素为(0,14,17,21,25)，
最小距离为3，即17-14；如果删除元素“2”和“14”，剩下的元素为(0,11,17,21,25)，
最小距离为4，即21-17 或者 25-21。
依次分析删除2个数的所有可能情况，可知最小距离的最大值为4。
'''
def check(a, m, x):
    k, c = 0, 0
    for i in range(1, len(a)):
        if a[i]-a[k] >= x:#当前距离不小于x，更新左边界
            c += 1
            k = i
    return c >= len(a) - 1 - m

def check2(a, m, x):
    k, c = 0, 0
    for i in range(1, len(a)):
        if a[i]-a[k] < x:#当前距离小于x，删除元素a[i]
            c += 1
        else: #否则更新左边界，处理下一条线段
            k = i
    return c <= m

def distance(a, m):
    left, right, ans = 1, a[-1], 0
    while left <= right:
        mid = (left + right) // 2
        if check(a, m, mid):
            ans = mid
            left = mid + 1
        else:
            right= mid - 1
    return ans

def distance2(a, m):
    left, right, ans = 1, a[-1], 0
    while left <= right:
        mid = (left + right) // 2
        if check2(a, m, mid):
            ans = mid
            left = mid + 1
        else:
            right= mid - 1
    return ans

def distance3(a, m):
    for ans in range(a[-1], 0, -1):
       if check(a, m, ans):
            return ans
        
def distance4(a, m):
    for ans in range(a[-1], 0, -1):
       if check2(a, m, ans):
            return ans

def min_pos(a):#返回最小距离的右边界
    p, d = 0, a[-1] + 1 #初始化最大值比实际最大值还大
    for i in range(1, len(a)):
        if a[i] > a[i-1] and a[i] - a[i-1] < d:
            p, d = i, a[i] - a[i-1]
    return p

def distance5(a, m):#贪心算法是不行的，需要用动态规划法
    def min_pos(a):#返回最小距离的右边界
        p = 1
        for i in range(2, len(a)):
            if a[i] - a[i-1] < a[p] - a[p-1]:
                p = i 
        return p
    b = list(a)
    p = min_pos(b) #寻找最小距离的右边界
    for i in range(m):
        del b[p]
        p = min_pos(b)  
    print(b, p, b[p])
    return b[p] - b[p-1]

a = (0,2,11,14,17,21,25)
for i in range(len(a)-1):
    print(distance(a, i), distance2(a, i), distance3(a, i),
          distance4(a, i), distance5(a, i))


    
