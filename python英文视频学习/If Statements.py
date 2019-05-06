

is_male=True  # Flase  # 两个变量进行检查
is_tall=True  # Flase

if is_male:
    print("you are a male")
    # 可以输入多行代码

else:
    print("you are not a male")

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male not are tall")
else:
    print("You neither not male or not tall or both")

























