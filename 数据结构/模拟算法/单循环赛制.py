#!/usr/bin/python3
# 文件名: 凯撒移位加密
# 作者：巧若拙
# 时间：2019-01-23
'''
单循环赛制是一种较为公平合理的比赛制度，比赛过程中所有参赛队伍均能相遇--次。
其秩序编排可采用“逆时针轮转方法”:
数字1~ n依次作为队伍编号，把编号按U型走向分成均等两边
(若n为奇数，则在末尾增加编号0，使总数为偶数)，即可得到第一轮的比赛秩序，
例如,有7个队参加比赛,比赛秩序编排如下所示:
第一轮 第二轮 第三轮 第四轮 第五轮 第六轮 第七轮
 1-0    1-7    1-6    1-5    1-4    1-3    1-2
 2-7    0-6    7-5    6-4    5-3    4-2    3-0
 3-6    2-5    0-4    7-3    6-2    5-0    4-7
 4-5    3-4    2-3    0-2    7-0    6-7    5-6
第二轮，固定编号1，其余编号均按逆时针方向移动-一个位置，即为该轮比赛秩序;
以后各轮比赛秩序以此类推，与编号0对阵的表示本轮轮空。
'''
def single_loop_system(n):
    t = list(range(1,n+1))
    if n % 2 == 1:
        t.append(0)
        n += 1
    for i in range(1, n):
        print(f'第{i}轮:', end=" ")
        for j in range(n//2):
            print(f'{t[j]}-{t[n-1-j]}', end="; ")
        print()
        temp = t[n-1]
        for j in range(n-1, 1, -1):
            t[j] = t[j-1]
        t[1] = temp

'''
从1985年起，世界性比赛多采用"贝格""编排法。
其优点是单数队参加时可避免第二轮的轮空队从第四轮起每场都与前一轮的轮空队比赛的不合理现象。
采用"贝格尔"编排法，编排时如果参赛队为双数时，
把参赛队数分一半(参赛队为单数时，最后以"0"表示形成双数)，
前一半由1号开始，自上而下写在左边;后一半的数自下而上写在右边，
然后用横线把相对的号数连接起来。
这即是第一轮的比赛。
第二轮将第一轮右上角的编号("0"或最大的一个代号数)移到左角上，
三轮又移到右角上，以此类推。
即单数轮次时"0"或最大的一个代号在右上角，双数轮次时则在左上角。
如下表示:
7 个队比赛的编排方法
第一轮 第二轮 第三轮 第四轮 第五轮 第六轮 第七轮
  1-0   0-5    2-0    0-6    3-0    0-7    4-0
  2-7   6-4    3-1    7-5    4-2    1-6    5-3
  3-6   7-3    4-7    1-4    5-1    2-5    6-2
  4-5   1-2    5-6    2-3    6-7    3-4    7-1
无论比赛队是单数还是双数，最后一轮时，
必定是"0"或最大的一个代号在右上角，"1"在右下角。
'''
def Berg_arrangement(n):
    t = list(range(1,n+1))
    if n % 2 == 1:
        t.append(0)
        n += 1
    for i in range(1, n):
        if i % 2 == 1:
            low, high = 1, n - 1
        else:
            low, high = 0, n - 2
        print(f'第{i}轮:', end=" ")
        for j in range(n//2):
            print(f'{t[j]}-{t[n-1-j]}', end="; ")
        print()
        #将右上角的编号移到左角上
        t[0], t[n-1] = t[n-1], t[0]
        for k in range(1, n//2):#逆时针移动n//2-1次
            temp = t[high]
            for j in range(high, low, -1):
                t[j] = t[j-1]
            t[low] = temp
        
single_loop_system(6)
Berg_arrangement(6)
