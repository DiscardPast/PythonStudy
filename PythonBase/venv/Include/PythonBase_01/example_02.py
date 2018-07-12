# ---***---   coding:utf-8   ---***---

"这是对于模块引入进行测试的脚本"

#引入一个系统模块
import time
#引入一个自定义模块
import example_01

#打印当前时间
print(time.time())
#查看example_01脚本文档
print(example_01.__doc__)
#打印example_01脚本变量new_Str
print(example_01.new_Str)
#调用example_01脚本方法hello()
print(example_01.hello())

"""
if (a==b) and (b==c) and c== d \
        or c==e and b==c and c==d \
        or c==e and b==c and c==d \
        or c==e and b==c and c==d \
        or c==e:
    pass
"""