# 变量指向函数
abs(-10)
print(abs)        # <built-in function abs>
# 赋值给变量
x=abs(-10)
print(x)
# 函数本身也可以赋值给变量
f=abs
print(f)          # <built-in function abs>

f=abs
print(f(-10))

# 函数名也是变量
# abs=10        # 函数名也是变量
# print(abs(-10))       # abs指向10后,abs这个变量已经不指向求绝对值函数而是指向一个整数10

# abs函数实际上是定义在import builtins模块中
# 要让修改abs变量的指向在其它模块也生效，
# 要用import builtins; builtins.abs = 10
import builtins
builtins.abs=10
print(builtins)     # <module 'builtins' (built-in)>
# print(abs(-10))
print(abs)          #  abs指向10后,就无法通过abs(-10)调用该函数了
# abs这个变量已经不指向求绝对值函数而是指向一个整数10

#  函数名也是变量，恢复abs函数，请重启Python交互环境


# 由于abs函数实际上是定义在import builtins模块中的
# 所以要让修改abs变量的指向在其它模块也生效，
# 要用import builtins; builtins.abs = 10


## 传入函数
# 高阶函数，即变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))



# def phoneWork(arg1,funcName,*arg2):
#     if(len(arg2)!=0):
#         funcName(arg1,arg2)
#     else:
#         funcName(arg1)
# def funCpu(arg1,arg2):
#     doSomeThing

max,min=min,max
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))

















