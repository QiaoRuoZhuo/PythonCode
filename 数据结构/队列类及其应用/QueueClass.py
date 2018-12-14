#!/usr/bin/python3

class QueueUnderflow(ValueError):
    pass


class ListQueue():  #列表实现循环队列类
    def __init__(self, len_=8):
        self.__len = len_
        self.__elems = [0] * len_ #默认每个元素都是0
        self.__head = 0 #队头元素下标
        self.__num = 0  #实际元素个数
        
    def __len__(self):
        return self.__num

    def is_empty(self):
        return self.__num == 0

    def peek(self):
        if self.__num == 0:
            raise QueueUnderflow("元素个数为0")
        return self.__elems[self.__head]

    def dequeue(self):
        if self.__num == 0:
            raise QueueUnderflow("元素个数为0")
        elem = self.__elems[self.__head]
        self.__head = (self.__head + 1) % self.__len
        self.__num = self.__num - 1
        return elem

    def enqueue(self, elem):
        if self.__num == self.__len:
            self.__extend()
        self.__elems[(self.__head + self.__num) % self.__len] = elem
        self.__num = self.__num + 1

    def __extend(self):
        old_len = self.__len
        self.__len *= 2
        new_elems = [0] * self.__len
        for i in range(old_len):
            new_elems[i] = self.__elems[(self.__head + i) % old_len]
        self.__elems, self.__head = new_elems, 0


class LNode():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
        

class LinkQueue(): #链表实现队列类
    def __init__(self):
        self.__head = None
        self.__rear = None

    def __len__(self):
        i, p = 0, self.__head
        while p:
            i += 1
            p = p.next
        return i

    def is_empty(self):
        return self.__head is None #只需用__head来判断是否为空队列

    def peek(self):
        if self.__head is None:
            raise QueueUnderflow("队列为空")
        return self.__head.elem

    def dequeue(self):
        if self.__head is None:
            raise QueueUnderflow("队列为空")
        p = self.__head
        self.__head = self.__head.next
        return p.elem
    
    def enqueue(self, elem):
        if self.__head is None:
            self.__rear = LNode(elem)
            self.__head = self.__rear
        else:
            self.__rear.next = LNode(elem)
            self.__rear = self.__rear.next


if __name__ == '__main__':
    lib = "123456789"
    s1 = ListQueue()
    s2 = LinkQueue()
    for i in lib:
        s1.enqueue(i)

    print(len(s1), len(s2))
    
    while not s1.is_empty():
        s2.enqueue(s1.peek())
        print(s1.dequeue())

    print(len(s1), len(s2))
    
    while not s2.is_empty():
        print(s2.dequeue())
