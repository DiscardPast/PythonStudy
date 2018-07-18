#  ---***---   coding:utf-8   ---***---

"本盘主要是通过查看str对象的帮助文档解决相关问题"

str = "    python是动态语言      "
print(str)
#查看str所具有的方法
print(dir(str))
#查看str的方法lstrip方法详细内容
"""
Help on built-in function lstrip:

lstrip(...) method of builtins.str instance
    S.lstrip([chars]) -> str
    
    Return a copy of the string S with leading whitespace removed.
    返回一个删除字符串S前置空格的复制
    If chars is given and not None, remove characters in chars instead.
    如果含有chars参数，则删除S中具有的chars
"""
help(str.lstrip)
#删除str的前置空格
print(str.lstrip())


# 查看str的方法rstrip方法详细内容
"""
rstrip(...) method of builtins.str instance
    S.rstrip([chars]) -> str
    
    Return a copy of the string S with trailing whitespace removed.
    返回一个删除字符串S后置空格的复制
    If chars is given and not None, remove characters in chars instead.
    如果含有chars参数，则删除S中具有的chars
"""
help(str.rstrip)
# 删除str的后置空格
print(str.rstrip())

# 查看str的方法strip方法详细内容
"""
strip(...) method of builtins.str instance
    S.strip([chars]) -> str
    
    Return a copy of the string S with leading and trailing whitespace removed.
    返回一个删除字符串S前置和后置空格的复制
    If chars is given and not None, remove characters in chars instead.
    如果含有chars参数，则删除S中具有的chars
"""
help(str.strip)
# 删除str的前置空格
print(str.strip())

s = "aBc"
#请将其全部大写
#查看s的方法
print(dir(s))
#猜测方法包含up...,则查看方法upper
help(s.upper)
"""
Help on built-in function upper:

upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.
"""
print(s.upper())

# 请将其全部小写
# 查看s的方法
print(dir(s))
# 猜测方法包含low...,则查看方法upper
help(s.lower)
"""
Help on built-in function upper:

lower(...) method of builtins.str instance
    S.lower() -> str
    
    Return a copy of the string S converted to lowercase.
"""
print(s.lower())


#查看s的类型
print(type(s))