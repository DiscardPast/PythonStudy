# ---***---   coding:utf-8   ---***---

"本章主要展示Python的基本数据类型"

#定义一个变量

#整型
a = 1
#查看它的id
print(id(a))
#查看它的类型
print(type(a))

#boolean
b = False
print(id(b))
print(type(b))

#list
c = [1,2,3]
print(id(c))
print(type(c))
c.append(4)
print(id(c))
print(type(c))

#tuple
d = (1,2,3,4)
print(id(d))
print(type(d))

#dict
d = dict(a='a', b='b', t='t')
print(d)

#
a = "123"
print(int(a) + 1)
