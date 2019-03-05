#!/usr/bin/python3
#文件：求解四宫数独
#作者：巧若拙
#日期：2019年2月19日
'''
四宫数独规则:在4x4的格子中，根据已知数字,推理出所有剩余空格的数字,
并满足每一行，每列，每一个宫内均含1到4的数字并且不重复,每道数独有且仅有唯一答案。
'''
def four_palace_sudoku(a, n):
    def answer(r, c):
        t = [0] * (n + 1)
        for i in range(n):#标记同行同列的已有数字
            t[a[r][i]], t[a[i][c]] = 1, 1
        s = int(n ** 0.5)#每个宫的尺寸
        #确定a[r][c]所在宫的起始行列坐标
        br, bc = (r // s) * s, (c // s) * s
        for i in range(br, br+s):#标记同宫已有数字
            for j in range(bc, bc+s):
                t[a[i][j]] = 1
        k = 0
        for i in range(1, n+1):
            if t[i] == 0:
                num = i
            else:
                k += 1 #累计已有数字
        if k == n - 1: #a[r][c]的值确定为num
            return num
        else:
            return 0
        
    flag = False
    while not flag:
        flag = True
        for r in range(n):
            for c in range(n):
                if a[r][c] == 0:
                    a[r][c] = answer(r, c)
                    if a[r][c] > 0:
                        flag = False
                        print(f'a[{r}][{c}] = {a[r][c]}')

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
    
def four_palace_sudoku2(a, n):
    def dfs(r, c):
        nonlocal count
        if r == n: #所有位置都填好了，输出解 
            count += 1
            print(f'{count}:')
            show(a, n)
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
    if a[0][0] > 0:
        dfs(0, 1)
    else:
        for i in range(1, n+1):
            if check(a, n, 0, 0, i):
                a[0][0] = i
                dfs(0, 1)
                a[0][0] = 0
                

a = [[0,4,0,0],
     [0,0,0,0],
     [0,0,3,0],
     [0,2,0,4]]
n = 4
show(a, n)
four_palace_sudoku(a, n)
show(a, n)

a = [[0,1,0,0],
     [0,0,0,0],
     [0,0,3,0],
     [0,2,0,0]]
n = 4
show(a, n)
four_palace_sudoku2(a, n)

