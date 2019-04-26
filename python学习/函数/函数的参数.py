# 位置参数
def power(x):
    return x+x
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
