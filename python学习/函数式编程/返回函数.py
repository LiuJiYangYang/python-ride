def calc_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax
# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

# 调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f=lazy_sum(1,3,5,7,9)
print(f)

# 调用函数f,求和
print(f())

# 函数lazy_sum中又定义了函数sum
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

f1=lazy_sum(1,3,5,7,9)
f2=lazy_sum(1,3,5,7,9)
print(f1)
print(f2)
print(f1==f2)
# f1()和f2()的调用结果互不影响

## 闭包
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return  i*i
        fs.append(f)
    return fs
f1,f2,f3=count()

print(f1())
print(f2())
print(f3())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
# 查看结果
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())
# 可利用lambda函数缩短代码

# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    def f():
        n=0
        while True:
            n=n+1
            yield n
    it = f()
    def counter():
        return next(it)
    return counter

counterA=createCounter()
print(counterA(),counterA(),counterA(),counterA(),counterA())


# 例二
def createCounter():
    a = [0]
    def counter():
        a[0]=a[0]+1
        return a[0]
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())

# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


