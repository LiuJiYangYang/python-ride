# if 语句
age=20
if age>=18:
    print('your age is',age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
# 完全可以用elif做更细致的判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
# elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
# if判断条件还可以简写
if 1:                  # 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
     print('True')
# input  最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思
# 这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情
s=input('birth:')
birth=int(s)
if birth<2000:
    print('00前')
else:
    print('00后')
# int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了
# s1=input('BMI:')
# BMI=int()
# if BMI<=18.5:
#     print('过轻')
# elif BMI>18.5 and BMI<=25:
#     print("正常")
# elif BMI>=25 and BMI<=28:
#     print('过重')
# elif BMI>28 and BMI<=32:
#     print('肥胖')
# elif BMI>32:
#     print('过重')
height=float(input('请输入你的身高：'))
weight=float(input('请输入你的体重：'))
bmi=weight/(height**2)
if bmi <=18.5:
    print('过轻')
elif bmi <=25:
    print('正常')
elif bmi <=28:
    print('过重')
elif bmi <=32:
    print('肥胖')
else:
    print('严重肥胖')

bmi=(80.5/(1.75*1.75))
print(bmi)

weight= float(input('请输入你的体重(kg)：'))
height= float(input('请输入你的身高(m)：'))
bmi=float(weight/(height**2))
if bmi<18.5:
    print('您的BMI值为','%.2f' % (bmi),'太轻了' )
elif bmi <=25:
    print('您的BMI值为','%.2f' % (bmi),'正常' )
elif bmi <= 28 :
    print('您的BMI值为','%.2f' % (bmi),'过重' )
elif bmi <= 32 :
    print('您的BMI值为','%.2f' % (bmi),'过度肥胖' )
else:
    print('你已经严重肥胖')

bmi = 80.5 /(1.75*1.75)
if bmi <18.5:
    print('过轻')
elif 18.5 <= bmi <25:
    print('正常')
elif 25 <=bmi<28:
    print('过重')
elif 28 <= bmi<32:
    print('肥胖')
else:
    print('严重肥胖')

h=input('身高：')
身高=float(h)
w=input('体重：')
体重=float(w)
y=float(体重//身高**2)
print('y=%.1f'%y)
if y<18.5:
    print('瘦猴')
elif 18.5<=y<25:
    print('匀称')
elif 25<y<=28:
    print('小胖胖')
elif 28<=y<32:
    print('中胖胖')
elif y>=32:
    print('大胖胖')

h=input('身高：')
身高=float(h)
w=input('体重：')
体重=float(w)
y=float(体重/(身高**2))

if y<18.5:
    print('y=%.1f' % y,'瘦猴')
elif 18.5<=y<25:
    print('y=%.1f' % y,'匀称')
elif 25<y<=28:
    print('y=%.1f' % y,'小胖胖')
elif 28<=y<32:
    print('y=%.1f' % y,'中胖胖')
elif y>=32:
    print('y=%.1f' % y,'大胖胖')