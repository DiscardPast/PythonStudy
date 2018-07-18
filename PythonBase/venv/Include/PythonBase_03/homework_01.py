# ---***---   coding:utf-8   ---***---

"Python基本数据类型第一小节习题"

info = 'abc'

print(info[2])
#会报错，因为这是个string类型的变量，其是不可变的，需要重新赋值只能重新赋值新的string值对象
#info[2] = 'd'
#如果要把上面的字符串info里面的c替换成d，要怎么操作呢？
info = 'abd'

a = '1'
b = 2
#a + b 的结果是什么
#报错，类型不对等
#print(a + b)
print(int(a) + b)