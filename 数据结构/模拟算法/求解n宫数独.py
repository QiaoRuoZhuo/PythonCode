#!/usr/bin/python3
#文件：求解n宫数独
#作者：巧若拙
#日期：2019年2月19日
'''
九宫数独规则:在9x9的格子中，根据已知数字,推理出所有剩余空格的数字,
并满足每一行，每列，每一个宫内均含1到9的数字并且不重复,每道数独有且仅有唯一答案。
'''
def check(a, n, r, c, num):#判断a[r][c]能否取数字num
    for i in range(n):#判断同行同列是否已有数字num
        if a[r][i] == num or a[i][c] == num:
            return False
    s = int(n ** 0.5)#每个宫的尺寸
    #确定a[r][c]所在宫的起始行列坐标
    br, bc = (r // s) * s, (c // s) * s
    for i in range(br, br+s):#判断同宫是否已有数字num
        for j in range(bc, bc+s):
            if a[i][j] == num:
                return False
    return True

def show(a, n):#输出结果
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print()
    print()

import copy
def sudoku(a, n):
    def is_ok(b, n):
        def answer(r, c):
            t = [0] * (n + 1)
            for i in range(n):#标记同行同列的已有数字
                t[b[r][i]], t[b[i][c]] = 1, 1
            s = int(n ** 0.5)#每个宫的尺寸
            #确定a[r][c]所在宫的起始行列坐标
            br, bc = (r // s) * s, (c // s) * s
            for i in range(br, br+s):#标记同宫已有数字
                for j in range(bc, bc+s):
                    t[b[i][j]] = 1
            k = 0
            for i in range(1, n+1):
                if t[i] == 0:
                    num = i
                else:
                    k += 1 #累计已有数字
            if k == n - 1: #b[r][c]的值确定为num
                return num
            else:
                return 0

        flag = False
        while not flag:
            flag = True
            for r in range(n):
                for c in range(n):
                    if b[r][c] == 0:
                        b[r][c] = answer(r, c)
                        if b[r][c] > 0:
                            flag = False
        #判定是否已经有解
        for i in range(n):
            for j in range(n):
                if b[i][j] == 0:
                    return False
        return True

    def dfs(r, c):
        nonlocal count
        b = copy.deepcopy(a)
        if is_ok(b, n) or r == n: #所有位置都填好了，输出解
            count += 1
            print(f'{count}:')
            show(b, n)
        elif a[r][c] > 0:#该位置的值已确定，直接下一步
            if c < n - 1:#确定下一个位置的坐标
                tr, tc = r, c + 1
            else:
                tr, tc = r + 1, 0
            dfs(tr, tc) 
        else:
            for i in range(1, n+1):#枚举本位置的可能取值
                if check(a, n, r, c, i):#如果可以取数字i，递归进入下一层
                    a[r][c] = i
                    if c < n - 1:
                        tr, tc = r, c + 1
                    else:
                        tr, tc = r + 1, 0
                    dfs(tr, tc)
            a[r][c] = 0 #所有数字都取过了，恢复原值，回溯
        
    count = 0
    dfs(0, 0)
              
a = [[0,1,0,0],
     [0,0,0,0],
     [0,0,3,0],
     [0,2,0,0]]
n = 4
show(a, n)
sudoku(a, n)

print()
a = [[1,0,8,0,0,4,0,5,0],
     [0,0,4,0,3,7,0,0,2],
     [0,0,2,0,0,6,4,3,0],
     [0,0,1,0,9,0,0,0,4],
     [5,7,0,4,8,0,0,6,3],
     [4,0,0,0,5,0,8,0,0],
     [0,9,5,1,0,0,3,0,0],
     [8,0,0,2,6,0,7,0,0],
     [0,1,0,3,0,0,9,0,8]]
n = 9
show(a, n)
sudoku(a, n)

print()
a = [[1,3,0,0,0,4,0,5,0],
     [0,0,4,0,0,0,0,0,2],
     [0,0,2,0,0,6,4,3,0],
     [0,2,1,0,9,0,0,0,4],
     [5,7,0,0,0,0,0,6,3],
     [4,0,0,0,5,0,8,0,0],
     [0,0,0,1,0,0,3,0,0],
     [8,0,0,0,0,0,7,0,0],
     [0,1,5,3,8,0,0,0,6]]
n = 9
show(a, n)
sudoku(a, n)

print()
a = [[8,0,0,0,0,0,0,0,0],
     [0,0,3,6,0,0,0,0,0],
     [0,7,0,0,9,0,2,0,0],
     [0,5,0,0,0,7,0,0,0],
     [0,0,0,0,4,5,7,0,0],
     [0,0,0,1,0,0,0,3,0],
     [0,0,1,0,0,0,0,6,8],
     [0,0,8,5,0,0,0,1,0],
     [0,9,0,0,0,0,4,0,0]]
n = 9
show(a, n)
sudoku(a, n)


