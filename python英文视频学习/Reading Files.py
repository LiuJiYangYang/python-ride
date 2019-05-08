employee_file=open("employees.txt","r")    #  读取想要的文件，r代表阅读

# print(employee_file.readable())
# print(employee_file.readline())     只读一行，打印多次读多行
# print(employee_file.readlines())    将所有内容放入一组数组中

for employee in employee_file.readlines():
    print(employee)


# print(employee_file.read())

employee_file.close()


# open("employees","r+")








