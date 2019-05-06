# tuples是一种数据类型的结构
coordinates=(4,5)  # 坐标
# coordinates[1]=10      # tuples是不可变的
print(coordinates[1])

# lists可变的
coordinates=[(4,5),(3.5),(8,9)]
coordinates[1]=(42,4)
print(coordinates)


# tuples中的lists可变
coordinates=(1,3,[3,4,5])
coordinates[2][0]=7

# coordinates[2]=[]      #  object does not support item assignment
print(coordinates)





