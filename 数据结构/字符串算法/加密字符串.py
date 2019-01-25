#!/usr/bin/python3
# 文件名: 加密字符串
# 作者：巧若拙
# 时间：2019-1-25

'''描述：字符串加密。待加密的n个字符(仅由ASCII码字符构成，最多支持960个字符)，加密方式如下：
①产生一个3到6之间的随机整数k, 将十进制数960均分成k份，字符在字符串中的位置除以k的余数决定该字符存放在第几份数据中(余数为1保存在第一份数据中，余数为2保存在第二份数据...余数为0保存在第k份数据中)；
②用十进制数127减去每个字符的ASCII码值，得到的差作为该字符的密文，同一段内的密文依次存放；
③将随机产生的数k加64后作为第一个密文存放到数组b中；
④将其他所有有密文按照在数据段中的位置依次逆序存放到数组b中；
⑤将数组b中的每个密文用3位数字保存，不足3位的前面用0补足，然后依次连接成一个新的字符串；
⑥返回密文字符串。
函数名：encrypt (p)
参数表：p –– 待加密的字符串。
返回值：c –– 加密后的字符串。
例1，当p = ”zp123”时，c=” 067078076015077005”；
例2，当p = ”Vb”时，c=” 068029041”。
'''

import random
    
def encrypt(p):
    k = random.choice((3, 4, 5, 6)) #3到6之间的随机整数k
    k = 3
    a = [-1] * 961 #默认均为-1
    t = 960 // k
    for i in range(len(p)):
        r, c = i % k, i // k
        a[r*t+c] = 127 - ord(p[i]) #将密文存储到数组a中
    a[960] = k + 64
    s = ['0'*(3-len(str(i))) + str(i) for i in a[::-1] if i != -1]
    return "".join(s)

def decrypt(s):
    k = int(s[:3]) - 64
    a = []
    for i in range(3,len(s),3):
        a.append(chr(127 - int(s[i:i+3])))
    a = a[::-1]
    b = [[0 for i in range(320)] for j in range(6)]
    rest = len(a) % k #有些列没有满，求出其余数
    width = len(a) // k #最小宽度，当所有的列都满时，刚好等于列数
    c, r, i = 0, 0, 0
    while i < len(a): #存储到二维数组中，以便提取明文
        if c < width or (c == width and r < rest):
            b[r][c] = a[i]
            c += 1
            i += 1
        else:
            r += 1
            c = 0
    p = []
    width += (rest > 0)
    for j in range(width): #从二维数组中提取明文
        for i in range(k):
            if b[i][j] != 0:
                p.append(b[i][j])
    return "".join(p)

p = "Vb"
s = encrypt(p)
print(s)
print(decrypt(s))
