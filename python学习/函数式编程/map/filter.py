# Python内建的filter()函数用于过滤序列
# 和map()不同的是，filter()把传入的函数依次作用于每个元素
## 然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))
# 一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','','B',None,'C',''])))

# filter求素数
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n
# 定义一个赛选函数
def _not_divisible(n):
    return lambda x:x%n>0
# 最后，定义一个生成器，
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


#  回数是指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
    return str(n) == str(n)[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# def is_palindrome(n):
#     n = str(n)
#     count = 0
#     while count<len(n):
#       return n[count] == n[len(n)-count-1]



def num_gen():#自然数迭代器
    n=1
    while True:
        yield n
        n=n+1

def hui_gen():#回数迭代器
    it=num_gen()
    it = filter(lambda x:str(x)==str(x)[::-1], it)
    while True:
        yield next(it)
for n in hui_gen():#测试
    if n<1000:
        print(n)
    else:
        break







