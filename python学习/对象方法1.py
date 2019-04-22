# 空List 有什么用？
a=[]
# append,给列表添加一个元素
a.append(1)
print(a)
# 注意append是向列表的尾部添加。如果我这时再添加一个元素2
a.append(2)
print(a)
# insert
a.insert(0,"hello")
print(a)
a.insert(1,'abc')
# 删除第一个元素 del和pop(删除后给个返回值)
del a[1]
a.pop(1)
print(a)
print(a.pop(1))
print(a)
# 从列表中删除第一个元素,后面出现的不做删除
a=[3,4,1,2,3,4]
a.remove(4)
print(a)
# reverse排序
a=[1,2,3,4,5]
a.reverse()
print(a)
# 首字母大写capitalize
print('HEllo'.capitalize())
