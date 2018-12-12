#!/usr/bin/python3
# 文件名: StackClass.py
from StackClass import ListStack,LinkStack


def check_parens(text):
    parens = "([{}])"
    opposite = {")":"(", "]":"[","}":"{"}
    #s = ListStack()
    s = LinkStack()

    for ch in filter(lambda x: x in parens, text):
        if ch in parens[:3]:
            s.push(ch)
        elif s.is_empty() or opposite[ch] != s.pop():
            return False
    else:
        return s.is_empty()


text = "({ [ f ] () }{})()"
print(check_parens(text))
    
