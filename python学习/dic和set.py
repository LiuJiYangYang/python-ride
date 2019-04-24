# Python内置了字典：dict的支持，dict全称dictionary,在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# 给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长
# 如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# 这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['Adam']=67
print(d['Adam'])
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Adam']=88
print(d['Adam'])     # 如果key不存在，dict就会报错
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
d['Thomas']=33
print('Thomas'in d)
print('dhsj'in d)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
d.get('Thomas')              # >>> d.get('Thomas')
print(d)                     # >>> d.get('Thomas', -1)
d.get('Thomas',-1)           # -1
print(d)                  # 注意：返回None的时候Python的交互环境不显示结果
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
d.pop('Bob')
print(d)
# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。dict是用空间来换取时间的一种方法。
# 在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象


# 哈希算法（Hash,这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
key=[1,2,3]
d[key] = 'a list'       # 而list是可变的，就不能作为key
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合
s=set([1,2,3])
print(s)
# 注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的
# 重复元素在set中自动被过滤
s=set([1,2,3,3,4,4])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(5)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)
print(s1 | s2)
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错
## str是不变对象，而list是可变对象,对list进行操作，list内部的内容是会变化的，
a=['c','b','a']
a.sort()
print(a)
# 而对于不可变对象，比如str，对str进行操作
a='abc'
a.replace('a','A')
a='abc'
b=a.replace('a','A')
print(b)
print(a)


l = ['a', 'b', 'c', 'a', 'b', 'a']
m = [1, 2, 3]
s = set(l)
print(s)
l1 = list(s)
print(l1)
l1.sort()
print(l1)
d = zip(l1, m)
print(dict(d))

lists = ['a', 'a', 'b', 'a', 'b', 'c']
d1={}
for i in lists:
    if lists.count(i)>=1:
        d1[i]=lists.count(i)
print(d1)

a=['a', 'a', 'b', 'a', 'b', 'c']
n=0
m=0
v=0
for x in a:
   if x=='a':
     n=n+1
     continue
   elif x=='b':
     m=m+1
     continue
   elif x=='c':
     v=v+1
     continue
d={'a':n,'b':m,'c':v}
print(d)

print(dict([(i, ['a','a','b','a','b','c'].count(i)) for i in set(['a','a','b','a','b','c'])]))