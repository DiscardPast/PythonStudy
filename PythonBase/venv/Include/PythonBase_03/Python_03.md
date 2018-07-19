# Python基本数据类型讲解(三)
## 1. 数据对象的类型
1. 不可变数据类型
    - string
    - int
    - tuple
    - 重新对变量赋值需要创建新的值对象，不可直接改变原有值对象的值
2. 可变数据类型
    - list
    - dict
    - 原有值对象对变量赋值可以被改变而不需要创建新的值对象
## 2. 再研究字符串
1. 三个引号的区别
    - ' '
    - " "
    - """ """
2. 偏移量
    - 字符串中字符的偏移量从0开始计数
3. 修改字符串
    - replace()
        - 返回一个新的在原有值对象上进行修改的值对象
        - 不是改变原有值对象
        - 例如:str = "abc",str.replace('a','ccc'),这会返回一个新的值对象cccdc
    - find()
        - 找到首个在字符串中与参数相匹配的子串的第一个字母的位置，如果找不到，返回-1
        - 例如:str = "hi and hi and hi",str.find('hi'),返回0，str.find('no')，返回-1
## 3. 格式化细究
1. %格式化方式
    - 占位符
        - %s占位字符串,%d占位整型
        - 数字可以自动适配%s
        - 数字字符('1234')不可自动适配%d
        - 基本占位示例
            - 'this is %s %d' % ('abcd',123)
        - 字典键值对占位方式
            - 'this is %(whose)s %(fruit)s' % {'fruit':'abcd','whose':123}
2. format格式化方法
    - 基本占位，类似于%
        - 'this is {} {}'.format('abcd',123)
    - 通过游标指定占位
        - 'this is {1} {0}'.format('abcd',123)
    - 通过键值对的方式指定占位
        - 'this is {whose} {fruit}'.format(fruit = 'abcd',whose = 123)
## 4. 文件操作
1. 基本方式
    - 打开文件
        - file = open('test.txt','w')
        - w write 写
        - r read 读
        - a append 追加
    - 操作文件
        - file.write('这是文件内容！')
    - 关闭文件
        - file.close()
    - 打开文件
        - file = open('test.txt'.'r')
    - 操作文件
        - print(file.readline(1))
    - 复位文件内容游标
        - file.seek(0)
2. linecatch
    - 读取文件
        - 读取某一行
            - linecache.getline('test.txt',1)
        - 读取所有
            - linecache.getlines('test.txt')
3. 看代码心态
    - 不要有代码崇拜，要敢于去看，去参考学习