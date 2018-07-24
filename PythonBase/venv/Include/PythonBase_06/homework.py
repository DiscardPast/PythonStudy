# ---***---   coding:utf-8   ---***---

"本章练习题"

"""
一: 已知：元组 a = (1,2,3) 利用list方法，输出下面的结果：

(1,2,4)

二: 利用列表推导完成下面习题：

1 输出结果：[1 love python,2 love python,3 love python,.... 10 love python]

2 输出结果：[(0,0),(0,2),(2,0),(2,2)]

三：

a = [1,2,3]

b = a[:]

del a

b的值是什么。为什么呢？
"""

#一
#本章主要考察对可变数据类型list和不可变数据类型tuple的理解，及list()的应用
a = (1,2,3)
b = list(a)
b[2] = 4
c = tuple(b)
print(c)

#二
print(['%s love python,' % x for x in range(1,11,1)])
print([(x,y) for x in range(3) for y in range(3) if x != 1 and y != 1])

#三
#删除指针a,b依然是指向[1,2,3]值引用的指针
a = [1,2,3]
b = a[:]
del a
print(b)