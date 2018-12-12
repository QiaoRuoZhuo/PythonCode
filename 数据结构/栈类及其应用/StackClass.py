#!/usr/bin/python3

class StackUnderflow(ValueError):
    pass


class ListStack():
    def __init__(self):
        self.__elems = []

    def __len__(self):
        return len(self.__elems)

    def is_empty(self):
        return self.__elems == []

    def top(self):
        if self.__elems == []:
            raise StackUnderflow("in ListStack.top()")
        return self.__elems[-1]

    def push(self, elem):
        self.__elems.append(elem)

    def pop(self):
        if self.__elems == []:
            raise StackUnderflow("in ListStack.top()")
        return self.__elems.pop()
    

class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
        

class LinkStack():
    def __init__(self):
        self.__top = None

    def __len__(self):
        i, p = 0, self.__top
        while p:
            i += 1
            p = p.next
        return i

    def is_empty(self):
        return self.__top is None

    def top(self):
        if self.__top is None:
            raise StackUnderflow("in LinkStack.top()")
        return self.__top.elem

    def push(self, elem):
        self.__top = LNode(elem, self.__top)

    def pop(self):
        if self.__top is None:
            raise StackUnderflow("in LinkStack.top()")
        p = self.__top
        self.__top = self.__top.next
        return p.elem
        

if __name__ == '__main__':
    lib = "12345"
    s1 = ListStack()
    s2 = LinkStack()
    for i in lib:
        s1.push(i)
    while not s1.is_empty():
        s2.push(s1.top())
        print(s1.pop())

    print(len(s1))
    print(len(s2))   
    while not s2.is_empty():
        print(s2.pop())
    print(len(s1))
    print(len(s2))
    
