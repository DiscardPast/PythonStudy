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

str = 'this is a example.'
print(str.find('a'))
print(str[8])
print(str.find('this'))
print(str.replace('this','that'))
print(str.find('no'))
str = 'hi and hi and hi'
print(str.find('hi'))
print(str[str.find('hi'):'hi'.__len__()])