# ---***---   coding:utf-8   ---***---

"本章主要讲解字符串相关内容"

a = "中国"

print(len(a))

#\n指换行，如果就是想要输出\n，需要在之前加一个\
a = 'abc\\n'
print(a)

a = "%s中国%s%d" % ("我是","人v",587)

print(a)

#字符串的游标
a = 'abcde'
#取出第一个字符
print(a[0])
#取出前三个字符
print(a[0:3])
#取出中间三个字符
print(a[1:4])
#取出所有字符
#a[0,len(a)),包含首位，不包含末位
print(a)
print(a[:])
print(a[0:])
print(a[0:len(a)])
#取出最后一个字符
print(a[len(a) - 1])
print(a[-1])


#替换字符串
#查看str的帮助文档
help("str")
str = "abcd"
print(str.replace("a","CCCCCCCCC"))
print(str)

#字符串拼接
a = "abc"
b = "1234"
#方法一
print(a+b)
#方法二
#%s占位字符串,%d占位整型
#数字可以自动适配%s
#数字字符不可自动适配%d
c = 56
print('字母:%s\n数字:%s%s' % (a,b,c))
#方法三
#性能更好
print('.'.join([a,b]))

#文件操作
d = open('a.txt','w')
d.write('hi.\nsecond hi.')
d.close()
d = open('a.txt','r')
print(d.readlines(200))
print(d.readlines(200))
d.seek(0)
print(d.readlines(200))
d.close()
