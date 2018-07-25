#   ---***----   coding:utf-8   ---***---

"本章主要展示Python数据类型元组的使用方法及特性"

#声明一个元组
a = (1,2,3)

#通过偏移量来获取数据
print(a[0])

#跳跃获取数据
print(a[0:2])

#查看元组的内置方法
print(dir(tuple))

#修改元组对象
#元组不可以像列表那样原地修改，以下修改方法是会重新生成一个元组对象
a = (1,2,3)
b = list(a)
b[2] = 4
print(id(a))
print(id(tuple(b)))
print(tuple(b))
#保证数据安全
def method(a):
    a[0] = 'ele0'
    return a
a = [1,2,3]
#报错，不可修改
#a = (1,2,3)
print(a)
method(a)
print(a)

#创建一个可变的集合对象
a = set('abcde')
print(a)
print(id(a))
a.add('cad')
print(a)
print(id(a))
a.update('ABC')
print(a)
print(id(a))
a.remove('a')
print(a)
print(id(a))
#a.remove('ccc')


#成员关系 in 和not in
b = 'c' in a
print(b)
b = 'c' not in a
print(b)

#交集&，并集|，差集-
a = set('abc1')
b = set('abc2')

#交集
print(a&b)
#并集
print(a|b)
#差集
print(a-b)

#set去重,列表内容重复
a = [1,1,2,2,2,3,4]
b = set(a)
print(b)
print(list(b))


#不可变集合
#无序，不可进行修改，添加操作
a = frozenset('abc')
print(a)
print('a' in a)
print('a' not in a)
#成员关系
a = frozenset('abc')
b = frozenset('abcd')
print(a&b)
print(a|b)
print(a-b)
#去重
a = [1,1,2,3,3,2,1,3]
b = frozenset(a)
print(b)