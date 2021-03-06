# 基础篇2-福利课python先入为主下篇
## 对变量，对象与赋值的浅析
### 1. 对象解析
1. 万事万物皆对象
    - 所有的数据类型都可以被看作对象
2. 一切变量都是对数据对象的一个引用
    - 对变量赋值，不是说这个变量就是这个值，而是这个变量指向了这个数据
3. Python内部的引用计数
    - 在Python中，可以用sys.getrefcount()方法可以查看当前数据的引用次数
    - 一个值的初始值不一定是0，因为Python内部在生成这个值对象的时候，会有一些机制会增加该值对象的引用计数。
    - 当每对一个值进行一次引用，则用sys.getrefcount()可以查看该值对象的引用计数，可以看到该值对象的引用计数加一
    - 当一个值对象的引用计数为0时，则会销毁该变量，实现自动回收
### 2. 变量的命名规范
1. 只能以字母和_开头
    - str/Str/_str
2. 不能使用关键字命名
    - 不能使用if/and/import/...等关键字命名
3. 合理的命名搭配方式
    - 文件名小写
    - 函数名小写
    - 变量小写
    - 可以使用_分割，例:new_str
    - 或者采用驼峰命名法:newStrTest
4. 大小写敏感
    - a和A是两个不同的变量
### 3. 变量的赋值
1. 动态特性
    - 在赋值时才会确定变量的类型
2. 多重赋值
    - 可以同时对多个变量进行赋值
3. 删除变量
    - del a
    - del a,b,c
### 4. 永远要记住
1. 三个内置对象
    - type()查看对象的类型
    - help()查看库的帮助文档
    - dir()查看模块的方法函数