# 调用abs函数
print(abs(100))
print(abs(-20))
print(abs(12.34))
# print(abs(1,2))   # 有且仅有一个参数
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型
# print(abs('a'))   # 也会报TypeError的错误，并且给出错误信息：str是错误的参数类型

# 而max函数max()可以接收任意多个参数，并返回最大的那个
print(max(1,2))
print(max(2,3,1,-5))
# 数据类型转换;Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a=abs
print(a(-1))

# Python内置的hex()函数把一个整数转换成十六进制表示的字符串
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

n1=122
n2=333
v1=hex(n1)
v2=hex(n2)
print('第一个值：%s\n第二个值：%s'  %(v1,v2))

n1 = 255
n2 = 1000
v1 = hex(n1)
v2 = hex(n2)
print('值1：%s \n值2: %s' % (v1,v2))