# 对象：数据和方法
# 对象数据
a='add214314'
# 对象方法
# count计算字符串中包含的多少个指定的子字符串
'1324 1313 435646'.count('123')
a='1324 1313 435646'
a.count('123')
print(a)
print(a.count('1313'))
# endswith 检查字符串是否以指定的字符串结尾
# startswith 检查字符串是否以指定的字符串开头
'139 13 789'.endswith('89')
print('139 13 789'.endswith('89'))
'185 123 789'.startswith('12')
print('185 123 789'.startswith('12'))
# 字符串对象的常用方法
# find 返回指定的字符串在字符串中的出现位置（不存在返回-1,位置从2开始包含第二位）
'1234567890'.find('24435')
print('1234567890'.find('24435'))
print('1234567890'.find('345'))
# 如果有多个，返回第一个，还可以指明从什么位置开始查找
'ok,good,name'.find(',')
print('ok,good,name'.find(','))
'ok,good,name'.find(',',3)
print('ok,good,name'.find(',',3))
print('ok,good,name'.find('k'))
print('ok,good,name'.find(','))
str1='001 come in,the name is jack,level 9,'
p0=str1.find('the name is')
p1=p0+len('the name is')
p2=str1.find(',',p1)
print(p0)
print(p1)
print(p2)
print(len('the name is'))
print(str1[p1:p2])
# 字符串对象的常用方法
# isalpha 检查字符串中是否都是字母
# isdigit 检查字符串中是否都是数字
'abd1'.isalpha()
'12311'.isdigit()
print('abd1'.isalpha())
print('12311'.isdigit())
# join 方法将 sequence类型的参数的元素合并成一个元素
a=['a','ds','sfs','sfdfs']
';'.join(a)
print(';'.join(a))
' '.join(a)
print(' '.join(a))
'+++'.join(a)
print('+++'.join(a))
# split 将字符串中的数字切割下来，生成新的元素；切割的字符串在原有的字符串中没有就显示原有的字符串
'123 456 789'.split('5')
print('123 456 789'.split('5'))
'123 456 789'.split('5')
print('123 456 789'.split('12343124'))
str1='001 name in,the name is jack,level9,'
print(str1.split('the name is')[1].split(',')[0])
# lower 将字符串里面如果有大写字母的全部转为小写字母
# upper 将字符串里面如果有小写字母的全部转为大写字母
'China'.lower()
'China'.upper()
print('China'.lower())
print('China'.upper())
# replace 替换字符串里面指定的子字符串
'Tom is a dog.Snoopy is a dog'.replace('dog','pig')
print('Tom is a dog.Snoopy is a dog'.replace('dog','pig'))
# strip 将字符串前置空格和后置空格删除
# lstrip 将字符串前置空格删除
# rstrip 将字符串后置空格删除
'  good  '.strip()
print('  good  '.strip())
'  good  '.lstrip()
print('  good  '.lstrip())
print('  good  '.strip())
# count 计算字符串中包含多少个指定的字符串
'djsdb,sdvf,dsdf'.count()
print('djsdb,sdvf,dsdf'.count())
# 空List 有什么用？
a=[]
# append,给列表添加一个元素
a.append(1)
print(a)