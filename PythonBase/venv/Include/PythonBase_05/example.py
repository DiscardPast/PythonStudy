# ---***---   coding:utf-8   ---***---

"本章主要演示list相关操作"

a = [1,2,3,4,5,6,7,8,9]

# 索引三个参数[起始位置:终止位置:遍历步长]
#正向索引
print(a[0:4:1])
#反向索引
print(a[-1:-5:-1])
#跳步索引
print(a[0:-1:2])
#默认索引
print(a[:])
print(a[:5:1])
print(a[4::2])

a = [1,2,3]
b = [4,5,6]

print(id(a))
print(id(b))
#a+b是重新创建了一个列表对象
print(id(a+b))
print(a + b)

#使用extend方法
#接收参数并将该参数的每个元素都添加到原有的列表中，是修改原有列表而不是创建新的列表
#extend参数为string或list,str会被处理为单个的字符
a = [1,2,3]
b = [4,5,6]
print('------------------------')
print(id(a))
print(a)
a.extend("str")
print(a)
print(id(a))
a.extend(b)
print(a)
print(id(a))

#使用append方法
#添加任意对象到列表的末端
a = [1,2,3]
print('------------------------')
print(a)
print(id(a))
a.append(4)
print(a)
print(id(a))
a.append([5,6,7])
print(a)
print(id(a))
a.append('str')
print(a)
print(id(a))
a.append(4)
print(a)
print(id(a))

#使用insert方法
#插入任意对象到任意位置
#如果输入位置参数大于位置最末位，则默认追加到最后一位，而不是空余越过的位置
a = [1,2,3]
print(a)
print(id(a))
print('------------------------')
a.insert(1,4)
print(a)
print(id(a))
a.insert(3,'str')
print(a)
print(id(a))
a.insert(17,[2,3,1])
print(a)
print(id(a))

#修改操作
#修改只需要对列表元素进行重新赋值即可，依然是在原有列表上更改，不会生成新的列表元素
print('###########################')
a = [1,2,3]
print(a)
print(id(a))
a[0] = 4
print(a)
print(id(a))
a[1] = 'str'
print(a)
print(id(a))


#删除操作
print('------------------------')
a = [1,2,3,4]
print(a)
#del方法

#删除列表a
del a
a = [1,2,3,4,5,6,7,8]
print(a)
#跳步删除列表元素
del a[::2]
print(a)
#删除单个列表元素
del a[0]
print(a)
#删除列表子串
del a[0:2]
print(a)
#remove方法
#删除列表中拥有的元素，如果列表中有多个元素重复，则删除第一个匹配到的该元素
# 如果元素不存在于列表，会报错
a = [1,2,3,4,4,4,5,6,7,8]
print(a)
a.remove(3)
print(a)
a.remove(4)
print(a)
#a.remove(10)
#print(a)

#pop出栈
#移除列表中最后一个元素
print(a.pop())
print(a)
print(a.pop())
print(a)

#成员关系
# in判断某元素是否在列表中，如果在返回True，不在返回False
# not in判断某元素是否不在列表中，如果不在返回True，在返回False
a = [1,2,3,4,5,6,7]
print(1 in a)
print(1 not in a)
print(8 in a)
print(8 not in a)


#列表推导式

#生成1到11步长为1的递增列表
print([x for x in range(1,11)])
#生成1到11步长为1，并且如果列表元素对2取余为0,也就是说是偶数，则加入列表，最后生成指定列表
print([x for x in range(1,11,1) if x % 2 == 0])

#列表排序和翻转
#sort方法对列表进行升序排列
#reverse方法对列表进行翻转
a = [7,4,2,5,1,9,3]
a.sort()
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.reverse()
print(a)
a.reverse()
print(a)
a.sort()
print(a)
#无论是sort()还是reverse()都是在原有列表上操作，不会生成新的列表对象
b = a.sort()
print(b)
b = a.reverse()
print(b)