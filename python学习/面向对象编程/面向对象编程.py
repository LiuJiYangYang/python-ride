# 面向过程的程序可以用一个dict
std1={'name':'Micheal','score':98}
std2={'name':'Bob','score':81}
print(std1)
print(std2)

def print_score(std):
    print('%s:%s'%(std['name'],std['score']))
print(std1)

# 对象拥有name和score这两个属性（Property)
class Student(object):
    def __init__(self, name, score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
# 类（Class）和实例（Instance）的概念是很自然的
# Class是一种抽象概念
# 实例（Instance）则是一个个具体的Student

class Student(object):
    """docstring for Student"""
    def init(self, name, score):
        super(Student, self).init()
        self.name = name
        self.score = score

def print_score(self):
    print('%s: %s' % (self.name, self.score))


class Student(object):
    def init(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def aa(self):
        if self.name !="于超":
            return 'A'
        elif self.age > 25:
            return "b"
        elif self.height > 150:
            return "C"
        else:
            return "D"
if __name__ == 'main':
    b=Student("于超",26,11)
    c=Student(1,26,150)
    print(b.aa())
    print(c.aa())



# __init__就是初始化这个类person的属性property
def __init__(self,name,age,height):
    self.name = name
    self.age = age
    self.height = height
# 下面是定义你将要创建的实例的技能
def paoniu(self):
    print('你可以泡妞啦')
def eat(self):
    print('你可以吃东西啦')
def printheight(self):
    print('你的身高是: %s' % self.height)
def printname(self):
    print('%s: %s' % (self.name, self.age))










