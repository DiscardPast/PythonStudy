# Python先入为主第一课(一)
### 1. Python是脚本解释型语言，C是编译型语言
#### 脚本解释型语言和编译型语言的编译原理
1. 脚本解释型语言
    1. 先把源代码（.py文件）编译成字节码文件（.pyc/.pyo文件）
    2. 再把字节码文件交给python虚拟机处理
    3. 虚拟机翻译成机器语言，交予机器执行  
2. 编译型语言
    1. 先把源代码文件翻译成机器语言
    2. 交予机器执行
3. 总结
    1. 脚本解释型与语言执行速率慢于编译型语言
    2. 但是脚本解释型语言可以一次编写处处运行
### 2. Python特性总结
1. 字节码
    - 可在虚拟机上执行，相当于一次编写处处运行
    - 第一次执行后，在之后的模块调用中会直接使用字节码
    - 会有一定的安全性，但是还是会被反编译
2. 动态语义
    - 是指在赋值时才会确定变量的类型
3. 缩进
    - 在Python中以缩进作为程序运行的分割点
    - 使用<tab>更为合适，一个tab相当于四个空格，在以后使用编辑器时，要进行设置并注意这个问题，否则可能出大问题
### 3. Python之禅（import this）
Beautiful is better than ugly.

优美胜于丑陋(Python以编写优美的代码为目标)

Explicit is better than implicit.

明了胜于晦涩（优美的代码应该是明了的，命名规范，风格相似）

Simple is better than complex.

简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）

Complex is better than complicated.

复杂胜于凌乱（如果复杂不可避免，那代码间也不要有难懂的关系，要保持接口简洁）

Flat is better than nested.

扁平胜于嵌套（优美的代码应该是扁平的，不应有太多嵌套）

Sparse is better than dense.

间隔胜于紧凑（优美的代码有适当的间隔，不要期望一行代码解决所有问题）

Readability counts.

可读性很重要（优美的代码是可读的）

Special cases aren't special enough to break the rules.

即使假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）

Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.

不要包容所有错误，除非你确定需要这样做（精准的捕获异常，不写except:pass风格的代码）

In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.

当存在多种可能，不要尝试去猜测。而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）

Although that way may not be obvious at first unless you're Dutch.

虽然这并不容易，因为你不是Python之父

Now is better than never.Although never is often better than *right* now.

做好过不做，但不假思索就开始还不如不做（动手之前细思量）

If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.

如果向人无法描述你的方案，那肯定不是一个好方案；反之亦然（方案评测标准）

Namespaces are one honking great idea -- let's do more of those!

命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）