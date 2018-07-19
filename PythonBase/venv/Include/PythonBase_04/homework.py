# ---***---   coding:utf-8   ---***---

"本章是有关与基本数据类型所学练习章节"

"""
一.已经字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。

二.在python中，如何修改字符串？

三.bool("2012" == 2012) 的结果是什么。

四.已知一个文件 test.txt，内容如下：

____________
2012来了。
2012不是世界末日。
2012欢乐多。
_____________

1.请输出其内容。
2.请计算该文本的原始长度。
3.请去除该文本的换行。
4.请替换其中的字符"2012"为"2013"。
5.请取出最中间的长度为5的子串。
6.请取出最后2个字符。
7.请从字符串的最初开始，截断该字符串，使其长度为11.
8.请将{4}中的字符串保存为test1.py文本.
 

五.请用代码的形式描述python的引用机制。

六.已知如下代码

________

a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' %a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
________

1.请给出str对象"中文编程"的引用计数
2.请给出str对象"python编程"的引用计数

七.已知如下变量
________
a = "字符串拼接1"
b = "字符串拼接2"
________

1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
2.请将a与b拼接成字符串c，并用逗号分隔。
3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
 

八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。

1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。
5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。

九.已知字符串
________

a = "i,am,a,boy,in,china"
________

1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
2.请使用2种办法取出其间的字符"boy"和"china"。
3.请找出第一个"i"出现的位置。
4.请找出"china"中的"i"字符在字符串a中的位置。
5.请计算该字符串一共有几个逗号。
 

十.请将模块string的帮助文档保存为一个文件。
"""

#一.已知字符串 s = "i,am,lilei",请用两种办法取出之间的“am”字符。

s = 'i,am,lilei'

#方法一
print(s.find('am'))
print(s[s.find('am'):s.find('am')+len('am')])
#方法二
print(s.find(','))
print(s.find(',',s.find(',') + 1))
print(s[s.find(',') + 1:s.find(',',s.find(',') + 1)])
#方法三
s.split(',')[1]

#二.在python中，如何修改字符串？
str = 'hello'
new_str = str.replace('h','H')
print(new_str)

#三.bool("2012" == 2012) 的结果是什么。    /False

print(bool("2012" == 2012))

"""
四.已知一个文件 test.txt，内容如下：

____________
2012来了。
2012不是世界末日。
2012欢乐多。
_____________

1.请输出其内容。
2.请计算该文本的原始长度。
3.请去除该文本的换行。
4.请替换其中的字符"2012"为"2013"。
5.请取出最中间的长度为5的子串。
6.请取出最后2个字符。
7.请从字符串的最初开始，截断该字符串，使其长度为11.
8.请将{4}中的字符串保存为test1.py文本.
"""

file = open('test.txt','w')
file.write(
"""2012来了。
2012不是世界末日。
2012欢乐多。""")
file.close()
file = open('test.txt','r')
str = file.read(2000)
# 输出文本内容
print(str)
# 该文本原始长度
print(len(str))
# 去除该文本原有换行
print(str.replace('\n',''))
# 请替换其中的字符"2012"为"2013"。
new_str = str.replace('2012','2013')
print(str.replace('2012','2013'))
# 取出最中间的长度为5的子串。
print(str[int(len(str)/2 - 2):int(len(str)/2 + 3)])
# 请取出最后2个字符。
print('************************')
print(str[-2:len(str)])
print(str[len(str) - 2:len(str)])
# 请从字符串的最初开始，截断该字符串，使其长度为11.
str = str[0 : 11]
print(str,len(str))
file = open('test.py','w')
file.write(new_str)
file.close()

file = open('test.py','r')
print(file.read(200))
file.close()

import sys
# 五.请用代码的形式描述python的引用机制。
a = "a"
print(id('a'))
print(id(a))
print(sys.getrefcount('a'))
b = 'a'
print(id('a'))
print(id(b))
print(sys.getrefcount('a'))
c = 'a'
print(sys.getrefcount('a'))
b = 'b'
print(sys.getrefcount('a'))
c = 'c'
print(sys.getrefcount('a'))


"""
六.已知如下代码

________

a = "中文编程"
b = a
c = a
a = "python编程"
b = u'%s' %a
d = "中文编程"
e = a
c = b
b2 = a.replace("中","中")
________

1.请给出str对象"中文编程"的引用计数
2.请给出str对象"python编程"的引用计数
"""

a = "中文编程"
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))
b = a
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))
c = a
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))
a = "python编程"
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))
b = u'%s' %a
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))
d = "中文编程"
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))
e = a
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))
c = b
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))
b2 = a.replace("中","中")
#print(sys.getrefcount("中文编程"))
print(sys.getrefcount("python编程"))

"""
七.已知如下变量
________
a = "字符串拼接1"
b = "字符串拼接2"
________

1.请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
2.请将a与b拼接成字符串c，并用逗号分隔。
3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
"""

#
a = "字符串拼接1"
b = "字符串拼接2"
c = a + b;
print(c)
c = "".join([a,b])
print(c)
c = "%s%s" % (a,b)
print(c)
c = "%(first)s%(second)s" % {'first' : a,'second' : b}
print(c)
c = "{}{}".format(a,b)
print(c)
c = "{0}{1}".format(a,b)
print(c)
c = "{first}{second}".format(first = a,second = b)
print(c)

c = ",".join([a,b])
print(c)
print(len(c))
print(c[6])

"""
八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。

1.包含0-9的数字。
2.所有小写字母。
3.所有标点符号。
4.所有大写字母和小写字母。
5.请使用你认为最好的办法将{1}-{4}点中的字符串拼接成一个字符串。
"""

import string
help(string)
print(string.digits)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.ascii_letters)
print("{digits}{ascii_lowercase}{punctuation}{ascii_letters}".format(digits = string.digits\
                                                                     ,ascii_lowercase = string.ascii_lowercase\
                                                                     ,punctuation = string.punctuation\
                                                                     ,ascii_letters = string.ascii_letters))


"""
九.已知字符串
________

a = "i,am,a,boy,in,china"
________

1.假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
2.请使用2种办法取出其间的字符"boy"和"china"。
3.请找出第一个"i"出现的位置。
4.请找出"china"中的"i"字符在字符串a中的位置。
5.请计算该字符串一共有几个逗号。
"""

a = "i,am,a,boy,in,china"
str = 'i,am,a,{sex},in,{country}'.format(sex = 'boy',country = 'china')
print(a[a.find('boy'):a.find('boy')+len('boy')])
print(a[a.find('china'):a.find('china')+len('china')])
print(a.split(',')[3])
print(a.split(',')[5])
# 方法一
print(a.find('i'))
print(a.find('china'))
print(a.find('i',14))
# 方法二
print(a.rfind('i'))


help('str')
help('str.count')
print(a.count(','))

# 十.请将模块string的帮助文档保存为一个文件。
file = open('string_help.txt','w')
str = string.__doc__
file.write(str)
file.close()

import sys
file = open('string_help_doc.txt','w')
sys.stdout = file
help(string)
file.close()