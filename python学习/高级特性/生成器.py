# 创建一个generator  第一种方法把一个列表生成式的[]改成()
L=[x*x for x in range(10)]
print(L)

g=(x*x for x in range(10))
print(g)
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator

# 打印出来，通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))        # 超出部分报错StopIteration
# print(next(g))

g=(x*x for x in range(10))
for n in g:
    print(n)

# 创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

a,b='b','a+b'
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]           # 但不必显式写出临时变量t就可以赋值

# 输出斐波那契数列的前N个数
print(fib(6))

# fib函数实际上是定义了斐波拉契数列的推算规则，
# 从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f=fib(6)
print(f)      # <generator object fib at 0x0000022BFC08FFC0>

# enerator和函数的执行流程不一样
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
o=odd()
print(next(0))
print(next(0))
print(next(0))
# print(next(0))         # 已经没有yield时，在执行会报错

# 函数改成generator后，不会用next（）来获取下一个返回值，而直接使用for循环来迭代
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib(6):
   print(n)

# for语句拿到generator的返回值，StopIteration错误，返回值包含StopIteration的value中
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib(6):
   print(n)

g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# 把每一行看做一个list，试写一个generator，不断输出下一行的list
def triangles():
    yield [1]
    l=[1]
    while True:
        s=[1]
        for i in range(len(l)-1):
            s.append(l[i]+l[i+l])
        s.append(l)
        yield s
        l=s

# 普通函数
r=abs(6)
print(r)
# generator函数
g=fib(6)
print(g)

# def triangles():
#     l = [1]
#     yield l
#     l.append(1)
#     yield l
#     while True:
#         x = l[:]
#         l = [1,1]
#         for i in range(1,len(x)):
#             l.insert(i, x[i-1] + x[i])
#         yield l

def triangles(t):
    n, l = 0, [1]
    while(n < t):
        yield l
        l = [1] + [l[i] + l[i + 1] for i,
                   v in enumerate(l) if len(l) > i + 1] + [1]
        n += 1
    return 'done'

for v in triangles(10):
    print(v)



#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list,写一个generater,不断输出下一行的list
def triangles():
    pass
# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]
# [1,5,10,10,5,1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')





# 要把fib函数变成generator，只需要把print(b)改为yield b就可以
# 函数定义中包含yield关键字，这个函数就不再是一个普通函数，而是一个generator
f=fib(6)
print(f)
