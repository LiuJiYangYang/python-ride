# 位置参数
def power(x):
    return x*x
# 当我们调用power函数时，必须传入有且仅有的一个参数x
print(power(5))
print(power(15))

# 计算xn
def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
power(5,2)
power(5,3)

# 默认参数

def power(x,n):
    s=1
    while n>0:
        s=s*x
    return s

def power (x, n:int=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5))
# 对于你>2，必须传入n,power(5,3)
print(power(5,3))
# 必选参数在前，默认参数在后
# 设置默认参数
def enroll(name,gender):
    print('name:',name)
    print('gender:',gender)
# 调用enroll()函数
a=enroll('Sarah','F')
print(a)            #   输出为None
# 传入参数
def enroll(name,gender,age=6,city="beijing"):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
# 提供两个参数，输出
enroll('Sarah','man')
# 于默认不符，输入相应的参数
enroll('Bob','M',7)
enroll('Adam','M',city='Tianjin')
# 默认参数降低调用的难度，可以传递更多的参数，调用只需要定义一个
def add_end(L=[]):
    L.append('END')
    return L
print(add_end([1,2,3]))
print(add_end(['x','y','z']))
# 默认参数调用
print(add_end())
# 再次调用，结果再原有基础上不断增加
print(add_end())
print(add_end())
# 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

# 用None实现   对象来实现
L=[]
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
add_end(L)
print(L)
print(add_end(L))
print(add_end())    # 无论调用多少次，都不会有问题
print(add_end())



def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
# 组装出一个list或tuple
print(calc([1,2,3]))
print(calc((1,3,5,7)))
# 简化
print(calc(1,2,3))
print(calc(1,3,5,7))

# 把函数参数改为可变参数
def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
# 定义可变参数，仅仅在参数前面加了一个*号；参数numbers接收到的是一个tuple,函数代码完全是不可变
# 调用该函数时，可以传入任意参数，包括0个参数
print(calc(1,2))
print(calc())

# 已有一个lis或者tuple,调用一个可变参数
sums=[1,2,3]
print(calc(sums[0]))
print(calc(sums[0],sums[1],sums[2]))    # 较为繁琐

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传
nums=[1,2,3]
print(calc(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去

# 关键字参数
# 可变参数传入0个或任意个参数，自动组装为一个tuple。关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
# 可以只传入默认参数
person('Michael',30)
person('Bob',35,city='Beijing')   # other变为dict
person('Adam',45,gender='M',job='Engineer')

# 先组装出一个dict,把该dict转换为关键字参数传进去
extra={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=extra['city'],job=extra['job'])

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)           # 简化
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

### 命名关键字参数
## 可以传入任意不受限制的关键字参数，可以通过kw检查
def person(name,age,**kw):
    if 'city' in kw:     # 有city参数
        pass
    if 'job' in kw:      # 有job参数
        pass
    print('name:',name,'age:',age,'other:',kw)
person('Jack',24,city='Beijing',addr='Chaoyang',zipcde=123456)

# 接收指定关键字
def person(name,age,*,city,job):
    print(name,age,city,job)
# 用*表示命名关键字参数分隔符
person('Jack', 24, city='Beijing', job='Engineer')

# 函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
def person(name,age,*args,city,job):
    print(name,age,args,city,job)
# 命名关键字参数必须传入参数名，没有传入参数名，调用将报错
person('Jack',24,'Beijing','Engineer')   # 报错，没有传入足够的参数


def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
# 命名关键字参数city具有默认值，调用时，可不传入city参数
person('Jack', 24, job='Engineer')

def person(name, age, city, job):  # 缺少 *，city和job被视为位置参数
    pass

# 必选参数、默认参数、可变参数、关键字参数和命名关键字参数
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)

f1(1,2,c=3)

f1(1,2,3,'a','b',x=99)

f2(1,2,d=99,ext=None)

args=(1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)

args=(1,2,3)
kw={'d':88,'x':'#'}
f2(*args,**kw)
# 计算两个数的乘积，改为接收一个或多个数并计算乘积
def product(x,y):
    return x*y
# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')




# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})
