a=1+2+3+4+5
# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
names=['Micheal','Bob','Tracy']
for name in names:
    print(name)
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

# 计算1-10的整数之和，可以用一个sum变量做累加
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
# 计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
list=list(range(30))
print(list)
# for list in list:
#     list=list+list
# print(list)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum=0
for x in range(101):
    sum=sum+x
print(sum)
# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

sum = 0
n = 1
while n < 100:
  sum = sum + n
  n = n + 2
print(sum)
# 在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出
# sum=0
# n=100
# while (n % 2)>0:
#     sum=sum+n
#     n=n-1
# print(sum)
#
# a=n%2
# print(a)
L = ['Bart', 'Lisa', 'Adam']
for l in L:
  print("Hello,%s!" % l)       # python 对缩进有强烈的要求
# break 再循环中，break语句可以提前退出循环
n=1
while n<=100:
    print(n)
    n=n+1
print('END')

n=1
while n<=100:
    if n>10:    # 当n = 11时，条件满足，执行break语句
        break   # break语句会结束当前循环
    print(n)
    n=n+1
print('END')         # break的作用是提前结束循环
# continue    在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
n=0
while n<10:
    n=n+1
    if n%2==0:      # 如果n是偶数，执行continue语句
        continue    # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)          #  计算相等于用==


L.pop('Bob')
