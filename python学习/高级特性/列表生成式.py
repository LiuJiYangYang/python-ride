# 列表生成式即List Comprehensions
# 创建list的生成式
# list[1,2,3,4,5,6,7,8,9,10]
print(list(range(1,11)))

L=[]
for x in range(1,11):
    L.append(x*x)
print(L)

print([x*x for x in range(1,11)])
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x*x for x in range(1,11) if x%2==0])

# 使用两层循环，生成全排列表
print([m+n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名，通过一行代码实现
import os    # # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')])   # # os.listdir可以列出文件和目录

# for循环可以使用两个或多个变量，dict的items（）可以同时迭代key和value
d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

# 列表生成式，使用两个变量生成list
d={'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])

# 把list中所有的字符串变成小写
L=['Hello','World','IBM','Apple']
print([s.lower() for s in L])

# list中既包含字符串，又包含整数
# 非字符串类型没有lower()方法，所以列表生成式会报错
L=['Hello','World',18,'Apple',None]
# print([s.lower() for s in L])         报错

# 内建的isinstance函数，判断是否是字符串
x='abc'
y=123
z=1.2334
print(isinstance(x,str))
print(isinstance(y,str))
print(isinstance(z,float))

# 修改列表生成式，通过添加if语句保证列表生成式能正确地执行
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [mystr.lower() for mystr in L1 if isinstance(mystr,str)]
print(L2)
# if L2==['hello', 'world', 'apple']:
#     print('输出')
# else:
#     print('输出')
