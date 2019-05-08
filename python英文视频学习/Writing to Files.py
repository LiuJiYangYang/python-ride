'''
# 编写和添加文件
employee_file=open("employees.txt","a")     # a是添加文件
# employee_file=open("employees.txt","w")   # w是重写文件

employee_file.write("\nKelly - Customer Service")
employee_file.write("Toby - Human Resources")

employee_file.close()
'''

'''
employee_file=open("employees1.txt","w")   # w是重写文件

employee_file.write("\nKelly - Customer Service")

employee_file.close()
'''

employee_file=open("index.html","w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()
