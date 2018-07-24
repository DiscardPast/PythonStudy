# ---***---   coding:utf-8   ---***---

"本章主要是展示list的应用以及前面所讲知识点的回顾和深入"

print(range(0,10,1)[5])

a = 'abcd'
print(list(a))
b = [1,2,3,4,5]
print(list(b))
print(list())
c = 1
#报错，因为int不可迭代
#print(list(c))
d = (1,2,3)
print(list(d))

for x in range(1000):
    if x %10 == 0:
        print(x)
for x in range(100):
    print(x * x)

#推导式再应用
#生成0~999的列表
print([x for x in range(1000)])
#生成0~999平方的列表
print([x * x for x in range(1000)])
#生成文章标题0~999的列表
print(['文章标题(%s)' % x for x in range(1000)])
#生成文章标题0~999的元组列表
print([(x,y,z)for x in range(10) for y in range(10) for z in range(10)])
#生成字典
a = dict([(x,y)for x in range(10) for y in range(10)])
print(a)

#翻来覆去再谈引用
a = ['1','2','3']
b = a
print(a)
print(id(a))
print(b)
print(id(b))
a[1] = 'c'
print(a)
print(id(a))
print(b)
print(id(b))
del b[1]
print(b)
print(a)
del b
#print(b)
print(a)

a = [1,2,3,4,5,6]
b = a

del a[::2]
print(a)
del a[0]
print(a)
del a[:]
print(a)
del a
#print(a)
print(b)