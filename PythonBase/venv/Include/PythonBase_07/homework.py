#   ---***----   coding:utf-8   ---***---

"本章习题"

"""
一 元组；a = (1,2,3)

1 有2种方法输出实现下面的结果：

(5,2,3)


2 判断2是否在元组里

二 集合a = set(['a','b','c'])做下面的操作：

1 添加字符串'jay'到集合a里。

2 集合b = set(['b','e','f','g']) 用2种方法求集合a 和集合b的并集。
"""

#一
a = (1,2,3)
b = list(a)
b[0] = 5
print(tuple(b))

a = (1,2,3)
b = set(a)
if 1 in b:
    b.remove(1)
b.add(5)
print(tuple(b))

#二
a = set(['a','b','c'])
print(a)
a.add('jay')
print(a)
b = set(['b','e','f','g'])
print(a|b)
print(a&b | a-b | b -a)