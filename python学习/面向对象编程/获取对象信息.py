# 使用type()
type(123)

type('str')

type(None)

# 变量指向函数或者类，用type()判断
type(abs)
print(type(abs))
# type(a)

# type(123)==type(456)

# type(123)==int

# type('abc')==type('123')

# type('abc')==str

# type('abc')==type(123)

import types
def fn():
    pass

type(fn)==types.FunctionType

type(abs)==types.BuiltinFunctionType

# type(lambda X:x)==types.LambdaType

type((x for x in range(10)))==types.GeneratorType


# 使用isinstance()
# object->Animal->Dog->Husky

# a=Animal()
# d=Dog()
# h=Husky()

# isinstance(h,Husky)

# h变量指向的就是Husky对象
# isinstance(h,Dog)

# isinstance(d, Dog) and isinstance(d, Animal)


# d不是Husky类型
# isinstance(d, Husky)




# 能用type()判断的基本类型也可以用isinstance()判断
isinstance('a', str)
isinstance(123, int)
isinstance(b'a', bytes)


# 并且还可以判断一个变量是否是某些类型中的一种，
# 比如下面的代码就可以判断是否是list或者tuple
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))

# 使用dir()
# 返回一个包含字符串的list,获得一个str对象的所有属性和方法
dir('ABC')






















