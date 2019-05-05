

lucky_numbers=[4,8,15,16,23,42]
friends=["Kevin","Karen","Jim","Oscar","Tim"]
# 在尾部添加另一个列表
friends.extend(lucky_numbers)
# 添加单个元素,在尾部
friends.append("Creed")
# 插入,   索引插入，，后面将向后移
friends.insert(1,"Kelly")
# 移除
friends.remove("Jim")
# 移除所有，输出空列表[]
friends.clear()
print(friends)

#
# friends.pop()

# 显示元素索引
# print(friends.index("Oscar"))   # 不存在，显示not in list

friends=["Jim","Jim","Jim","Jim","Kevin","Karen"]
print(friends.count("Jim"))

# 列表进行排序，升序排列
friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

# 将list反过来
lucky_numbers.reverse()
print(lucky_numbers)

# 复制副本
friends2=friends.copy()
print(friends2)

