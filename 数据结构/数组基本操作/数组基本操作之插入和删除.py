#!/usr/bin/python3
# 文件名: 数组基本操作之插入和删除
# 作者：巧若拙
# 时间：2018-12-17

'''
例题1.将指定对象x插入数组a的指定位置index。
python中用insert()方法实现该功能。
语法：list.insert(index, obj)
参数说明：index -- 对象obj需要插入的索引位置。
          obj -- 要插入列表中的对象。
返回值：方法没有返回值，但会在列表指定位置插入对象。
我们今天编写自定义函数my_insert()实现相同功能，要注意修正索引的值：
语法：my_insert(list, index, obj)
参数说明：list -- 被处理的列表。
          index -- 对象obj需要插入的索引位置。
          obj -- 要插入列表中的对象。
返回值：方法没有返回值，但会在列表指定位置插入对象。
'''
def my_insert(a, index, x):
    if index >= len(a):
        index = len(a)
    elif index + len(a) <= 0:
        index = 0
    elif index < 0:
        index += len(a)

    a.append(x)
    i = len(a) - 1
    while i > index:
        a[i] = a[i-1]
        i -= 1
    a[i] = x

'''
同步训练1.已知a是非递减列表，请将对象obj插入到a的适当位置，并保证a的有序性。
语法：insert_obj(list, obj)
参数说明：list -- 被处理的列表。
          obj -- 要插入列表中的对象。
返回值：方法没有返回值，但会在列表适当位置插入对象。
'''
def insert_obj(a, x):
    a.append(x)
    i = len(a) - 2
    while a[i] > x:
        a[i+1] = a[i]
        i -= 1
    a[i+1] = x
    

'''
例题2.移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
python中用pop()方法实现该功能。
语法：list.pop([index=-1])
参数说明：index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，
                   默认为 index=-1，删除最后一个列表值。
返回值：该方法返回从列表中移除的元素对象。
我们今天编写自定义函数my_pop()实现相同功能：
语法：my_pop(list, index=-1)
参数说明：list -- 被处理的列表。
          index -- 要移除列表元素的索引值。
返回值：返回从列表中移除的元素对象，同时更新原列表。
'''
def my_pop(a, index=-1):
    x = a[index]
    del a[index]
    return x

'''
例题3.移除列表中某个值的第一个匹配项。
python中用remove()方法实现该功能。
语法：list.remove(obj)
参数说明：obj -- 列表中要移除的对象。
返回值：该方法没有返回值，但是会移除列表中的某个值的第一个匹配项。
我们今天编写自定义函数my_remove()实现相同功能：
语法：my_remove(list, obj)
参数说明：list -- 被处理的列表。
          obj -- 列表中要移除的对象。
返回值：该方法没有返回值，但是会移除列表中的某个值的第一个匹配项。
'''
def my_remove(a, x):
    del a[a.index(x)]


'''
同步训练3.移除列表中某个值的最后一个匹配项。
语法：remove_last(list, obj)
参数说明：list -- 被处理的列表。
          obj -- 列表中要移除的对象。
返回值：该方法没有返回值，但是会移除列表中某个值的最后一个匹配项。
'''
def remove_last(a, x):
    for i in range(len(a)-1,-1,-1):
        if a[i] == x:
            del a[i]
            break

    
'''
课后练习3.以较高效率删除数组a中所有值为x的元素。
语法：remove_all(list, obj)
参数说明：list -- 被处理的列表。
          obj -- 列表中要移除的对象。
返回值：该方法没有返回值，但是会删除数组a中所有值为x的元素
'''
def remove_all(a, x):
    i, j = 0, 0
    for e in a:
        if e == x:
            j += 1
        else:
            a[i] = a[i+j]
            i += 1
    del a[i:]
    

a = ['Google', 'Runoob', 'Taobao']
a.pop(1)
print(a)

a = ['Google', 'Runoob', 'Taobao']
print(my_pop(a))
print(a)

a = [1,2,2,3,4,3,2,2,2,1,2,1]
remove_last(a, 2)
print(a)
remove_last(a, 2)
print(a)
remove_all(a, 2)
print(a)
a = [1,2,2,3,4]
insert_obj(a, 5)
print(a)
insert_obj(a, 1)
print(a)
