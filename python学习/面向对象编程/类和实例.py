# 定义类是通过class关键字
class Student(object):
    pass


# 定义Student类，根据Student类创建出Student的实例，创建实例是通过类名+（）实现
bart=Student
print(bart)      # 变量bart指向的就是一个Student的实例,后面的0x10a67a590是内存地址
print(Student)

bart.name='Bart Simpson'
print(bart.name)           #  bart一个name属性

# 类可以起到模板的作用，可以在创建实例，可以绑定的属性强制填写进去
# 通过定义一个特殊的__init__方法，创建时绑定name,score等属性
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
# 注意到__init__方法的第一个参数永远是self

bart=Student('Bart Simpson',59)
print(bart.name)
print(bart.score)

# 数据封装
def print_score(std):
    print('%s:%s'%(std.name,std.score))
print_score(bart)




class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
bart=Student('Bart Simpson',59)
print(bart.name)
print(bart.score)
print(bart.print_score())


class Student(object):
    def get_garde(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.age = 8
print(bart.age)
# lisa.age
# print(lisa.age)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'age'


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())



def print_score(self):
    print('姓名：%s 分数：%d'%(self.name,self.score))
def get_grade(self):
    if self.score>=90:
        return 'A'
    elif self.score>=60:
        return 'B'
    else:
        return 'C'
# 创建类的实例
student_a = Student('tangchunli', 100)
student_b = Student('zhangsanfe', 60)

student_a.print_score()
print(student_a.name,student_a.score, student_a.get_grade())

student_b.print_score()
print(student_b.name, student_b.score, student_b.get_grade())








