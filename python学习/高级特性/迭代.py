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

# 判断      通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
# True
isinstance([1,2,3], Iterable) # list是否可迭代
# True
print(isinstance(123, Iterable)) # 整数是否可迭代
# False

# enumerate函数 把list变成索引-元素对，在for循环中同时迭代索引和元素
for i,value in enumerate(['A','B','C']):
    print(i,value)

# for循环，同时引用两个变量
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

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

