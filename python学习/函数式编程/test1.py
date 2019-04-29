L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def num(list):
    return list[1]
print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]))
print(sorted([('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)],key=num, reverse=True))



