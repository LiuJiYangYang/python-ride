# Unicde编码是2个字节，ASCII是一个字节
print('包含中文的str')
a=ord('A')  # ord()函数获取字符的整数表示
print(a)
a=ord('中')
print(a)
#  chr()函数把编码转换为对应的字符
a=chr(66)
print(a)
a=chr(25991)
print(a)
# 知道字符串的整数编码，用十六进制这么写str
print('\u4e2d\u6587')
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表
x=b'ABC'
print(x)
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
str='ABC'.encode('ascii')
print(str)
str='中文'.encode('utf-8')
print(str)      #  使用'中文'.encode('ascii')会报错
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
str=b'ABC'.decode('ascii')
print(str)
str=b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(str)
# 如果bytes中包含无法解码的字节，decode()方法会报错
a=b'\xe4\xb8\xad\xff'.decode('utf-8')
print(a)
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
a=b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(a)
# 要计算str包含多少个字符，可以用len()函数
str=len('ABC')
print(str)
str=len('中文')
print(str)
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
str=len(b'ABC')
print(str)
str=len(b'\xe4\xb8\xad\xe6\x96\x87')
print(str)
str=len('中文'.encode('utf-8'))
print(str)
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
# 在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换
# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
#!/usr/bin/env python3
# -*- coding: utf-8 -*-      第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
# 如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文


# 格式化字符串,在Python中，采用的格式化方式和C语言是一致的，用%实现
a='hello,%s'%'world'
print(a)
a='Hi,%s,you have $%d.'%('Michael',100000)
print(a)
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
#占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print('Age:%s.Gender:%s'%(25,True))
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate:%d %%'%7)
# format()
# 另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
s1=85-72
print('小明成绩提升：%.2f%%'%(100*(85-72)/72))
print('72.{0:.1f}%'.format(100*(85-72)/72))
# Python 3的字符串使用Unicode，直接支持多语言。

# 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。Python当然也支持其他编码方式，比如把Unicode编码成GB2312
print('中文'.encode('gb2312'))
# 牢记仅使用UTF-8编码