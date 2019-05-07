# try:
#     number=int(input("Enter a number: "))
#     print(number)
# except:       # 高亮显示
#     print("Invalid Input")
'''
# value=10/0     # 报错
try:
    value=10/0           # 跳过输入提示进行下一步
    number=int(input("Enter a number: "))
    print(number)
except:       # 高亮显示
    print("Invalid Input")
'''

# value=10/0     # 报错
try:
    value=10/0           # 跳过输入提示进行下一步
    number=int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("err")
except ValueError:
    print("invalid input")


