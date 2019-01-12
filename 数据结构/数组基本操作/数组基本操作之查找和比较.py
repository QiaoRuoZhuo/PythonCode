#!/usr/bin/python3
# 文件名: 数组基本操作之查找和比较
# 作者：巧若拙
# 时间：2018-12-17


'''
数组的操作是算法中最最基本的内容。
虽然Python的list内置了很多基本函数，能够方便地实现数组的一些基本操作，
但是如果能够自己来实现这些基本函数，才算真正理解了其内在原理，才能在实际应用中融会贯通。
'''
'''
例题1.统计某个元素在列表中出现的次数。
python中用count()方法实现该功能。
语法：list.count(obj)
参数说明：obj -- 列表中统计的对象。
返回值：返回元素在列表中出现的次数。
我们今天编写自定义函数my_count()实现相同功能：
语法：my_count(list, obj)
参数说明：list -- 被访问的列表。
          obj -- 列表中统计的对象。
返回值：返回元素在列表中出现的次数。
'''
def my_count(a, x):
    s = 0
    for e in a:
        if e == x:
            s += 1
    return s

'''
同步训练1.统计某个字符串中字母和数字的个数。
语法：count_alnum(str)
参数说明：str -- 被访问的字符串。
返回值：(alpha, digit)分别表示字母和数字的个数。
'''
def count_alnum(s):
    alpha, digit = 0, 0
    for e in s:
        if (e >= "A" and e <= "Z") or (e >= "a" and e <= "z"):
            alpha += 1
        elif e >= "0" and e <= "9":
            digit += 1
    return (alpha, digit)


'''
例题2.返回列表元素中的最大值的下标（索引值）。
python中用max(list)方法返回列表元素中的最大值，但没有返回其下标。
我们可以联合使用max(list)和list.index(obj)方法来实现该功能，也可以自定义函数实现相同功能。
我们今天编写自定义函数max_pos()实现相同功能：
语法：max_pos(list)
参数说明：list -- 要返回最大值下标的列表。
返回值：返回列表元素中的最大值的下标。
'''
def max_pos(a): 
    pos = 0
    for i in range(1, len(a)):
        if a[i] > a[pos]:
            pos = i
    return pos

'''
同步训练2.以较高效率同时返回列表元素中的最大值和最小值的下标。
语法：max_min_pos(list)
参数说明：list -- 要返回最值下标的列表。
返回值：(maxpos, minpos)分别表示最大值和最小值的下标。
'''
def max_min_pos(a): 
    maxpos, minpos = 0, 0
    for i in range(1, len(a)):
        if a[i] > a[maxpos]:
            maxpos = i
        elif a[i] < a[minpos]:
            minpos = i
    return (maxpos, minpos)


'''
例题3.返回列表元素中比对象obj大的最小值，若找不到这返回obj。
我们可以联合使用列表生成式和min(list)方法返回该最小值，也可以自定义函数实现相同功能：
语法：my_min(list, obj)
参数说明：list -- 被访问的列表。
          obj -- 被比较的对象。
返回值：返回列表元素中比对象obj大的最小值，若找不到这返回obj。
'''
def my_min(a, x):
    m, p = x, 0
    while p < len(a) and a[p] <= m:
        p += 1
    if p < len(a): #先找到第一个满足条件的元素
        m = a[p]
        
    for e in a[p+1:]:#再去找满足条件的最小值
        if e > x and e < m:
            m = e
    return m

'''
例题4.判断列表是否为非递减序列。
语法：is_non_decreasing(list)
参数说明：list -- 被访问的列表。
返回值：若列表为非递减序列，返回True;否则返回False。
'''
def is_non_decreasing(a):
    for i in range(1, len(a)):
        if a[i] < a[i-1]:  
            return False
    else:
        return True

'''
同步训练4.输出列表中递增子序列的数量。
语法：inc_seq_num(list)
参数说明：list -- 被访问的列表。
返回值：返回列表中递增子序列的数量。
'''
def inc_seq_num(a):
    s = 1
    for i in range(1, len(a)):
        if a[i] <= a[i-1]:  
            s += 1

    return s


'''
课后练习1.已知元组t存储了若干个正整数，请编写函数返回元组中奇数的数量。
语法：odd_num(tuple)
参数说明：tuple -- 存储了正整数的元组。
返回值：返回元组中奇数的数量。
'''

'''
课后练习1_2.给定一个字符串,在字符串中找到第一个至少连续出现k次的字符。
语法：find_first(s, k)
参数说明：s -- 给定的字符串。
          k -- 正整数，表示某个字符至少连续出现的次数
返回值：若存在返回该字符，否则返回"No"。
例如：s="abcccaaab",k=3，则返回"c"
'''
def find_first(s, k):
    c = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:  
            c += 1
            if c == k:
                return s[i]
        else:
            c = 1
    else:
        return "No"


'''
课后练习2.已知元组t存储某个班级所有学生的身高，请编写函数返回班级的平均身高。
语法：average(tuple)
参数说明：tuple -- 存储了学生身高的元组。
返回值：返回班级的平均身高。
'''

'''
课后练习3.以较高效率同时返回列表元素中的最大值和次大值的下标。
语法：max_sec_pos(list)
参数说明：list -- 要返回最值下标的列表。
返回值：(maxpos, secpos)分别表示最大值和次大值的下标。
'''
def max_sec_pos(a): 
    maxpos, secpos = 0, 0
    for i in range(1, len(a)):
        if a[i] > a[maxpos]:
            secpos, maxpos = maxpos, i
        elif a[i] > a[secpos]:
            secpos = i
    return (maxpos, secpos)

'''
课后练习4.返回列表的最长递增子序列。
语法：max_inc_seq(list)
参数说明：list -- 被访问的列表。
返回值：返回列表的最长递增子序列a[l:r]。
'''
def max_inc_seq(a):
    left, max_left, length, max_length = 0, 0, 1, 1
    for i in range(1, len(a)):
        if a[i] > a[i-1]:  #继续递增
            length += 1
            if max_length < length: #更新最优左边界和最大长度
                max_left, max_length = left, length
        else: #设置新子序列的左边界和初始长度
            left, length = i, 1   

    return a[max_left : max_left + max_length]

'''
课后练习5.已知元组t存储了若干个正整数，请编写函数返回相邻元素差值最大值。
语法：max_difference(tuple)
参数说明：tuple -- 存储了正整数的元组。
返回值：返回相邻元素差值最大值。
示例：对于元组a=(3,2,2,4,3,5)，返回2；对于元组a=(3,6,2,4,3,5)，返回4
'''
def max_difference(t):
    m = 0
    for i in range(1, len(t)):
        if abs(t[i]-t[i-1]) > m:
            m = abs(t[i]-t[i-1])
    return m

'''
课后练习6.返回最长连续字母串。
输入一个只包含大写字母的非递减字符串，返回最长连续字母串（忽略重复字母）
语法：max_inc_str(upper_string)
参数说明：upper_string -- 被访问的非递减字母串。
返回值：返回最长连续字母串。
示例：对于字符串upper_str="ABBBBDEEFGIJKMMMMMM"，返回"DEFG"。
'''
def max_inc_str(a):
    max_letter, length, max_length = a[0], 1, 1
    for i in range(1, len(a)):
        if ord(a[i]) > ord(a[i-1]) + 1: #非连续字母串，更新字母串长度
            length = 1
        elif ord(a[i]) == ord(a[i-1]) + 1: #连续字母串
            length += 1
            if max_length < length: #更新最大字母和最大长度
                max_letter, max_length = ord(a[i]), length

    left = max_letter - max_length + 1 #连续字母串的起始字母的ASCII 数值
    s = []
    for i in range(left, left+max_length):
        s.append(chr(i))
    return ''.join(s)


a="ABBBBDEEFGIJKMMMMMM"
print(find_first(a, 56))
print(max_inc_str(a))

a = [1,2,3,3,4,5,6,6,7]
for e in a:
    print(e, ":", a.count(e), " -- ", my_count(a, e))

b = "1234abcdEFG ……￥5678hIJK"
print(count_alnum(b))

p1 = a.index(max(a))
p2 = max_pos(a)
print(p1, a[p1], "---", p2, a[p2])
p3, p4 = max_min_pos(a)
print(p3, a[p3], "---", p4, a[p4])
p5, p6 = max_sec_pos(a)
print(p5, a[p5], "---", p6, a[p6])

print(my_min(a, 3))

print(is_non_decreasing(a))
print(inc_seq_num(a))
print(max_inc_seq(a))

t = (3,6,2,4,3,5)
a = rank(t)
print(a)

print(max_difference(t))


