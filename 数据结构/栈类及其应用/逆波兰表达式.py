#!/usr/bin/python3
# 文件名: StackClass.py
from StackClass import ListStack,LinkStack


def translate(line): #转换为逆波兰表达式
    operators = "()+-*/"
    priority = {"(":1, "+":2, "-":2, "*":3, "/":3}
    s = ListStack()
    exp = [] #用来存储逆波兰表达式

    def tokens(line):
        i, tlen = 0, len(line)
        while i < tlen:
            while line[i].isspace(): #去除多余空格
                i += 1
            if i >= tlen:
                break
            
            if line[i] in operators: #处理运算符
                yield line[i]
                i += 1
            else:                    #处理运算对象
                j = i + 1
                while (j < tlen and not line[j].isspace() and
                       line[j] not in operators):
                    if (line[j] in ('e','E') and
                        j+1 < tlen and line[j+1]=='-'): #处理负指数
                        j += 1
                    j += 1
                yield line[i:j]
                i = j
                    
    for x in tokens(line):
        if x not in operators:
            exp.append(x)
        elif s.is_empty() or x == "(":
            s.push(x)
        elif x == ")":
            while not s.is_empty() and s.top() != "(":
                exp.append(s.pop())
            if s.is_empty():
                raise SyntaxError("Missing '('.")
            s.pop() #左括号出栈
        else:
            while (not s.is_empty() and
                   priority[s.top()] >= priority[x]):
                exp.append(s.pop())
            s.push(x) #运算符入栈

    while not s.is_empty():
        if s.top() == "(":
            raise SyntaxError("Extra '('.")
        exp.append(s.pop())

    return exp


def compValue(exp): #求逆波兰表达式的值
    operators = "+-*/"
    s = ListStack()

    for x in exp:
        if x not in operators:
            s.push(float(x))
            continue

        if len(s) < 2:
            raise StackUnderflow("Short of operand(s).")
        b = s.pop()
        a = s.pop()

        if x == "+":
            c = a + b
        elif x == "-":
            c = a - b
        elif x == "*":
            c = a * b
        elif x == "/":
            c = a / b

        s.push(c)

    if len(s) != 1:
        raise StackUnderflow("Extra operand(s).")
    return s.pop()


def main():
    while True:
        try:
            line = input("请输入算术表达式：")
            if line.strip() == "": return
            res = compValue(translate(line))
            print(line, "=" , res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)

text = "30*(1.5+2.5) - 600/6"
print(translate(text), "=", compValue(translate(text)))
main()


    
