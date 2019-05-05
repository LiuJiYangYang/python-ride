# sys模块，hello的模块

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

import sys

if __name__=='__main__':
    test()

# $ python3 hello.py      # 命令行执行

# $ python hello.py Michael   # 命令行执行

# 启动Python交互环境，再导入hello模块
# $ python3
# import hello           # 没有打印Hello, word!
# 有执行test()函数。
#
# 调用hello.test()时，才能打印出Hello, word!

# hello.test()


### 作用域


# private函数或变量不应该被别人引用
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 调用greeting()函数不用关心内部的private函数细节，
# 这也是一种非常有用的代码封装和抽象的方法

# 外部不需要引用的函数全部定义成private
# 只有外部需要引用的函数才定义为public


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

def addFunc(a,b):
    return a+b

print('atestmodule计算结果:',addFunc(1,1))













