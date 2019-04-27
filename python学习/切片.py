L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0])
print([L[0], L[1], L[2]])
# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环
r=[]
n=3
for i  in range(n):
    r.append(L[i])
print(r)
# 一行代码就可以完成切片
print(L[0:3])


# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符
a='ABCDEFG'[:3]
print(a)
a='ABCDEFG'[::2]
print(a)


# 实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    return s
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

while s[:1] == ' ':
    s=s[1:]
while s[-1:] == ' ':
    s=s[:-1]
# return


