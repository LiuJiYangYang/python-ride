# for (i=0; i<list.length;i++){
#     n=list[i];
# }

d={'a':1,'b':2,'c':3}
for key in d:
    print(key)

# 默认情况下，dict迭代的是key
# for value in d.values()

# 同时迭代key和value
# for k, v in d.items()

for ch in 'ABC':
    print(ch)
# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以使用isinstance()判断一个对象是否是Iterable对象
# 判断      通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
# True
isinstance({}, Iterable)
# True
isinstance([], Iterable)
# True
isinstance((x for x in range(10)), Iterable)
# True
isinstance([1,2,3], Iterable) # list是否可迭代
# True
print(isinstance(123, Iterable)) # 整数是否可迭代
# False

from collections import Iterator
isinstance((x for x in range(10)),Iterator)
# True
isinstance([],Iterator)
# False
isinstance({},Iterator)
# False
isinstance('abc',Iterator)
# False
isinstance(iter([]), Iterator)
# Ture
isinstance(iter('abc'),Iterator)
# Ture

# Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的

for x in [1,2,3,4,5]:
    pass

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


def triangles():
    L=[1]
    while True:
        yield L
        L=[L[-1]+2]+[L[i]+L[i+1] for i in range(len(L)-1)]+[L[-1]+1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

# def fib2(max):
#     n, a, b = 0, 0, 1
#     arr = []
#     while n < max:
#         arr.append(b)
#         a, b = b, a + b
#         n = n + 1
#     return arr

def triangles():
    tri=[1]
    while 1:
        yield tri
        t=[tri[0]+2]
        tri=t+[tri[i]+tri[i+1] for i in range(len(tri)-1)]+t

n=0
results=[]
for t in triangles():
    print(t)
    results.append(t)
    n=n+1
    if n==10:
        break





# enumerate函数 把list变成索引-元素对，在for循环中同时迭代索引和元素
for i,value in enumerate(['A','B','C']):
    print(i,value)

# for循环，同时引用两个变量
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

# 使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    return (None, None)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')




def L(L):
  if L != [] :
    if len(L) ==1:
        return (L[0],L[0])
    else:
        min_index = L[0]
        max_index = L[0]
        for i in L:
            if min_index >= i:
                min_index = i
            else:
                min_index
            if max_index <= i:
                max_index = i
            else:
                max_index
        return (min_index,max_index)
  else:
    return (None, None)

