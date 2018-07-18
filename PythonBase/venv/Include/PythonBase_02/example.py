# ---***---   coding:utf-8   ---***---

"本章主要解析Python中变量的相关属性"


import sys
import time
#将一个整形数据4赋值给变量d
d = 4
a = 4
print(type(d))
#将一个字符串对象hello赋值给d
d = "hello"
print(type(d))


#对象的引用计数示例
str = "test"
print(sys.getrefcount("test"))
str1 = "test"
print(sys.getrefcount("test"))
str2 = "test"
print(sys.getrefcount("test"))
str = "test1"
print(sys.getrefcount("test"))
str1 = "test2"
print(sys.getrefcount("test"))

#变量命名
str = 4
new_str = 4
#大小写敏感
a = 5
A = 5
#多重赋值
a,b,c = 3,"hell0","true"
print(a)
print(b)
print(c)

print(A)
#删除变量
del A
#出错，不存在变量A
#print(A)
#删除元祖
del a,b,c
#出错，a,b,c未被定义
#print(a)

#help文档去帮助我们了解Python的模块
help(time)
help(time.sleep)

#dir
print(dir(time))