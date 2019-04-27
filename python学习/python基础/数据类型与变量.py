# 数据类型  整数 浮点数 字符串
# 转义字符 \   换行 \n  制表符 \t    字符\用\\表示
print('I\'m ok')
print('I\'m learning\npython')
print('\\\n\\')
print('\\\t\\')
# r''默认字符不转义
print(r'\\\t\\')
# '''...'''表示多行内容,多行输入提示符>>>变为...   注意...是提示符，不是代码的一部分
print('''linel
...line2
...line3
''')
# 输入'''和括号)后，执行该语句并打印结果
print('''linel
line2
line3
''')
print('line1\nline2\nline3')
# 多行字符串'''...'''还可以在前面加上r使用,引号里面为字符串
print('''hello,\n
world''')
# 布尔值  Ture和False
a=3>2
print(a)
a=3>5
print(a)
# 布尔值可以用and、or和not运算；and为与运算，只所有都为Ture，and运算结果才为Ture
a=True and True
print(a)
a=True and False
print(a)
a=False and False
print(a)
a=5>3 and 3>1
print(a)
# not运算是非运算，它是一个单目运算符，把True变成False，False变成True
a=not 1>2
print(a)
# 布尔值经常遇到条件判断中
if a >= 18:
    print('adult')
else:
    print('teenager')
# None是一个特殊的空值，None不代表0，0是有意义的
# python还提供了列表、字典等多种数据类型，还允许创建自定义数据类型，
#    变量;等号=是赋值语句，同一个变量可以反复赋值
a=1
t_007='T007'
Answer=True   # 变量Answer是一个布尔值Ture/。
a=123 # a是整数
print(a)
a='ABC' # a变为字符串
print(a)
# 动态语言和静态语言，动态语言相对于静态语言较为灵活
a='ABC'
# python 解释器干了两件事，一个是创建"ABC"的字符串，一个创建一个名为a的变量，并把它指向'ABC'
a='ABC'
b=a
a='XYZ'
print(b)   # 执行结果ABC
# 常量，不能变的量；通常用全部是大写的变量名表示常量
PI=3.12131
# python中通常用/和//表示除法；//称为地板除，所除结果永远为整数
print(10/3)
print(9/3)
print(10//3)
# 取余
print(10%3)


n = 123
print(n)
f = 456.789
print(f)
s1 = 'Hello, world'
print(s1)
s2 = 'Hello, \'Adam\''
s3=r'Hello, "Bart"'
print(s3)
a="r'''Hello"
print(a)







