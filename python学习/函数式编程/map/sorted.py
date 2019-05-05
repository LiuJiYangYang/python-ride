# 排序算法
# Python内置的sorted()函数就可以对list进行排序
print(sorted([36,5,-12,9,-21]))

# 按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

list=[36,5,-12,9,-21]

keys=[36,5,12,9,21]

# sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素
# keys排序结果 => [5, 9,  12,  21, 36]
#                 |  |    |    |   |
# 最终结果     => [5, 9, -12, -21, 36]

print(sorted(['bob','about','Zoo','Credit']))
# 给sorted传入key函数，即可实现忽略大小写的排序
print(sorted(['bob','about','Zoo','Credit'],key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# -*- coding: utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def num(list):
    return list[1]
print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]))
print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)],key=num, reverse=True))



L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def fn1(x):
    return x[0]

def fn2(x):
    return x[1]

print(sorted(L,key=fn1))
print(sorted(L,key=fn2))

def by_name(t):
    return sorted(t,key=lambda x:x[0])

def by_name(t):
    return sorted(t,key=lambda x:x[1],reverse=True)





















