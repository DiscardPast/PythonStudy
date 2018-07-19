# ---***---   coding:utf-8   ---***---

"""
1：

a = 'pyer'

b = 'apple'

用字典和format方法实现：

my name is pyer, i love apple.


2:打开文件info.txt,并且写入500这个数字。


"""

a = 'pyer'
b = 'apple'

print('my name is %s, i love %s.' % (a,b))
print('my name is %(a)s, i love %(b)s.' % {'a': 'pyer','b':'apple'})

print('my name is {}, i love {}.'.format(a,b))
print('my name is {0}, i love {1}.'.format(a,b))
print('my name is {aT}, i love {bT}.'.format(aT = 'pyer',bT = 'apple'))


file = open('info.txt','w')
file.write('500')
file.close()
file = open('info.txt','r')
print(file.read(20))
file.close()

import linecache
print(linecache.getline('info.txt',1))
print(linecache.getlines('info.txt'))
