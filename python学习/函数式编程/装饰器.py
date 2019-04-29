# 函数也是一个对象，函数对象可以被赋值给变量
def now():
    print('2015-3-25')
f=now
print(f())

# 函数对象有一个_name_属性
# now._name_
# f._name_

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 要借助Python的@语法，把decorator置于函数的定义
@ log
def now():
    print('2015-3-25')

# 运行now()函数前打印一行日志
print(now())

# 把@log放到now()函数的定义
now=log(now)
print(now)

# log()是一个decorator，返回一个函数
# 原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
# 于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数

# wrapper()函数的参数定义是(*args,**kw),wrapper()函数可以接受任意参数的调用

# decorator的高级函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

print(now())

# 两层嵌套的decorator相比，3层嵌套的效果是这样的
now=log('execute')(now)
print(now)

now.__name__
print(now.__name__)     # 返回'wrapper'
# 需要把原始函数的__name__等属性复制到wrapper()函数中,否则会报错

# 不需要编写wrapper.__name__ = func.__name__这样的代码
# Python内置的functools.wraps就是干这个事的
import functools
def log(func):
    @functools.wraps(func)
    def warpper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return warpper

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
# 针对带参数的decorator
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s%s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator



#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
# -*- coding: utf-8 -*-
import time, functools
def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
@log
def f():
    pass
@log('execute')
def f():
    pass

import functools

def log(arg):
    if isinstance(arg, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(arg)
                print('begin call')
                fn = func(*args, **kw)
                print('end call')
                return fn
            return wrapper
        return decorator
    else:
        @functools.wraps(arg)
        def wrapper(*args, **kw):
            print('begin call')
            fn = arg(*args, **kw)
            print('end call')
            return fn
        return wrapper

@log
def f1():
    print('f1')

f1()

@log('execute')
def f2():
    print('f2')

f2()



##
# -*- coding: UTF-8 -*
def log(func):
    def decorator(func1):
        def wrapper(*args, **kw):
            print('begin call')
            result = func1(*args, **kw)
            print('end call')
            return result
        return wrapper

    if isinstance(func, str):
        return decorator
    else:
        return decorator(func)

@log
def f():
    print('f is invoked')

print(f.__name__)
f()


import functools
import time

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        fn = func(*args, **kwargs)
        end = time.time()
        print('%s() execute in %s ms' % (func.__name__, (end - start) * 1000))
        return fn
    return wrapper












#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)



