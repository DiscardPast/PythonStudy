# ---***---   coding:utf-8   ---***---

"Python数据类型再次详解(三)"

#不可变类型
test = 'abc'
print(test[0])
#test[0] = 'd'

#可变类型
test = ['a','b','c']
print(test)
test[0] = 'd'
print(test)

# '/"/"""的区别
a = 'abc"'
b = "abc'"
c = """
'abc"'"'
"abc'"'"
"""
print(a)
print(b)
print(c)

#如何修改字符串之replace,find
str = 'this is a example.'
print(str.find('a'))
print(str[8])
print(str.find('this'))
print(str.replace('this','that'))
print(str.find('no'))
str = 'hi and hi and hi'
print(str.find('hi'))
print(str[str.find('hi'):'hi'.__len__()])
print(str.find('hi',len('hi')))
print(str[7] + str[8])

#格式化细究

#%
print('this is %s %d' % ('abcd',123))
print('this is %(whose)s %(fruit)s' % {'fruit':'abcd','whose':123})

#format(方法)
print('this is {} {}'.format('abcd',123))
print('this is {1} {0}'.format('abcd',123))
print('this is {whose} {fruit}'.format(fruit = 'abcd',whose = 123))


#文件操作
file = open('test.txt','w')
file.write("first line\nsecond line\nthird line")
file.close()
file = open('test.txt','r')
print(file.readlines(20))
print(file.readlines(20))
file.seek(0)
print(file.readline(5))
file.close()

#Python内置模块
import linecache
help(linecache)
help(linecache.getline)

print(linecache.getline('test.txt',1))
print(linecache.getline('test.txt',2))
print(linecache.getline('test.txt',3))
print(linecache.getline('test.txt',1))

print(linecache.getlines('test.txt'))