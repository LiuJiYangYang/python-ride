# 设定参数的默认值，可以降低函数调用的难度
int() # 函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换
int('12345')
# int()函数还提供额外的base参数，默认为10。传入base参数，就可以做N进制的转换
int('12345',base=8)

int('12345',16)

# 转换大量的二进制字符串
def int2(x,base=2):
    return int(x,base)

int2('10000000')
int2('10101010')

# functools.partial 创建一个偏函数
import functools
int2 = functools.partial(int, base=2)
int2('10101110')
int2('10101010')

import functools
int2 = functools.partial(int, base=2)
print(int2('1000000',base=10))

int2=functools.partial(int,base=2)
print(int2)
# 相当于
kw={'base':2}
int('10010',**kw)

max2=functools.partial(max,10)

# 把10作为*args的一部分自动加到左边
max2(5,6,7)
print(max2(5,6,7))

args=(10,5,6,7)
print(max(*args))


import functools

def add(*args, **kwargs):
    print(*args)
    print('-' * 20)
    for key, value in kwargs.items():
        print('%s : %s' % (key, value))

add_partial = functools.partial(add, 10, k1 = 10, k2 = 20)
add_partial(1, 2, 3, k1 = 40, k3 = 30)








