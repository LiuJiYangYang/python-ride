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

bart=Student('Bart Simpson',59)
print(bart.score)
bart.score=99
print(bart.score)

# 要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 实例的变量名如果以__开头，就变成了一个私有变量（private）

# 实例变量.__name
# 实例变量.__score
# bart.__name       报错

class Student(object):
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
# 给Student类增加set_score方法
# class Student(object):
#     def set_score(self,name):
#         self.__score = score
# 方法中，可以对参数做检查，避免传入无效的参数
class Student(object):
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')
# _name, 虽然我可以被访问，但是，请把我视为私有变量，不要随意访问
bart._Student__name

# 错误写法
bart=Student('Bart Simpson',59)
bart.get_name()

bart.__name='New Name'   # 设置__name变量
bart.__name


bart.get_name()  # get_name()内部返回self._name



# 把下面的Student对象的gender字段对外隐藏起来，
# 用get_gender()和set_gender()代替，并检查参数有效性
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)












