# ---***---   coding:utf-8   ---***---


"""
1 字符串:

a = 'abcd'

用2个方法取出字母d
"""
a = 'abcd'

print(a[-1])

print(a[len(a) - 1])

"""
2：

a = 'jay'

b = 'python'

用字符串拼接的方法输出：

my name is jay,i love python.
"""
a = 'jay'

b = 'python'

print('my name is %s,i love %s' %(a,b))


a = 'www'

b = 'baidu'

c = 'com'

d = '.'.join([a,b,c])

e = d.split('.')
print(e)