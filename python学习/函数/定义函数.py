# 定义函数
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-99))
print(my_abs(99))
# 空函数
# pass占位符
def nop():
    pass
age=int()
if age >= 18:
    pass
# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
my_abs(1, 2)
# 如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别
my_abs('A')
abs('A')
# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善
# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# 添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误
my_abs('A')
# 返回多个值
# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数
x,y=move(100,100,60,math.pi / 6)
print(x,y)
# 但其实这只是一种假象，Python函数返回的仍然是单一值
r=move(100,100,60,math.pi / 6)
print(r)

import math
math.sqrt(2)

# ??????????????
# x = 0
# if b*b- 4*a*c < 0:
#    x = "无解"
#
# if b*b - 4*a*c >= 0:
#    x = ((-b + math.sqrt(b*b - 4*a*c)) / (2*a),(-b - math.sqrt(b*b - 4*a*c)) / (2*a))
# return x

# ??????????????
# def quadratic(a, b, c):
#     if not isinstance(a, (int, float)):
#         raise TypeError('bad operand type')
#     if not isinstance(b, (int, float)):
#         raise TypeError('bad operand type')
#     if not isinstance(c, (int, float)):
#         raise TypeError('bad operand type')
#     tj = b*2 - 4ac
#     if tj < 0:
#         return "无实数根"
#     else:
#         return (-b+math.sqrt(tj))/2a, (-b-math.sqrt(tj))/2*a