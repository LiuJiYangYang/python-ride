# python是内建map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

#               f(x)=x*x

#                   │
#   ┌───┬───┬───┬───┼───┬───┬───┬───┐
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
# [ 1   2   3   4   5   6   7   8   9 ]
#
#   │   │   │   │   │   │   │   │   │
#   │   │   │   │   │   │   │   │   │
#   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼
#
# [ 1   4   9  16  25  36  49  64  81 ]

def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
# map()传入的第一个参数是f，即函数对象本身
# r是一个Iterator，Iterator是惰性序列
def f(n):
    return n*n
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

# 把这个list所有数字转为字符串
list(map(str,[1,2,3,4,5,6,7,8,9]))
print(list)
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
print(map(str,[1,2,3,4,5,6,7,8,9]))
print((str,[1,2,3,4,5,6,7,8,9]))

# reducereduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

# reduce(f,[x1,x2,x3,x4])=f((f(x1,x2),x3),x4)

from functools import reduce
def add(x,y):
    return x+y
reduce(add,[1,3,5,7,9])
print(reduce(add,[1,3,5,7,9]))
# 求和运算可以直接用Python内建函数sum()，没必要动用reduce

from functools import reduce
def fn(x,y):
    return x*10+y
reduce(fn,[1,3,5,7,9])
print(reduce(fn,[1,3,5,7,9]))

# 考虑到字符串str也是一个序列，配合map()改动
# 把str转换为int的函数
from functools import reduce
def fn(x,y):
    return x*10+y
def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
reduce(fn,map(char2num,'13579'))
print(reduce(fn,map(char2num,'13579')))

# 整理成一个str2int的函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

# lambda函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

# -*- coding: utf-8 -*-
def normalize(name):
    newname = name[0].upper()
    n = 1
    while True:
        newname = newname + name[n].lower()
        n = n + 1
        if n == len(name):
            break
    return newname
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
# -*- coding: utf-8 -*-
from functools import reduce
def prod(x):
    def mx(x,y):
        return x*y
    return reduce(mx,x)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

from functools import reduce
def prod(L):
    return reduce(lambda x, y: x * y,list(L))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# from functools import reduce
# def prod(x):
#     def mx(x,y):
#         return x*y
#     return reduce(mx,x)
#
# L1=[1,2,3,4,5,6]
# sum=list(sum(prod,L1))

# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]
def str2float(s):
    a = s.split('.')
    a[1]=a[1][::-1]
    return reduce(lambda x,y:x*10+y,map(char2num,a[0])) + reduce(lambda x,y:x/10+y,map(char2num,a[1]))/10

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
   print('测试成功!')
else:
   print('测试失败!')





