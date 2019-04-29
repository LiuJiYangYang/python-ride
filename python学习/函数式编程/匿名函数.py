# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

# 匿名函数lambda  x: x*x
def f(x):
    return x*x
# 匿名函数也是一个函数对象
f=lambda x: x*x
print(f)
# 也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
print(f(5))

def build(x,y):
    return lambda:x*x+y*y
print(build(5,4))


# -*- coding: utf-8 -*-
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)


def is_old(n):
    return lambda:n%2== 1
l = list(filter(is_old,range(1,20)))
print(l)


# def is_old(n):
#     return
# L1 = list(filter(lambda n: n % 2 == 1, range(1, 20)))
# print(L1)












