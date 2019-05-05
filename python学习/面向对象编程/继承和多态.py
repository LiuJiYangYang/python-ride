# 可以从某个现有的class继承，新的class称为子类Subclass，
# 而被继承的class称为基类、父类或超类(Base class、Super class)

class Animal(object):
    def run(self):
        print('Animal is running...')

# 编写Dog和Cat类     从Animal类继承
class Dog(Animal):
    pass
class Cat(Animal):
    pass

# Cat和Dog是Animal的子类
dog=Dog()
dog.run()

cat=Cat()
cat.run()

# Animal is running...         运行结果
# Animal is running...

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')

# 子类的run（）覆盖了父类的run(),在代码运行的时候，总是会调用子类的run()，我们就获得了继承的另一个好处：多态
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

# 判断一个变量是否是某个类型可以用isinstance()判断
isinstance(a,list)
isinstance(b,Animal)
isinstance(c,Dog)

isinstance(c,Animal)    # c不仅仅是Dog，c还是Animal

b=Animal()
isinstance(b,Dog)       # Dog可以看成Animal，但Animal不可以看成Dog

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())     # 打印出来

run_twice(Dog())

run_twice(Cat())

# 定义一个Tortoise类型，也从Animal派生
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

print(run_twice(Tortoise()))


class Timer(object):
    def run(self):
        print('Start...')
# 动态语言的“鸭子类型”，它并不要求严格的继承体系


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)


class Animal(object):
    def run(self_a):
        print('Animal is running...')
    def run_twice (bnimal): #跟self一樣，也就是說可以不必叫self self
        bnimal.run()
        bnimal.run()
        print(bnimal)

class Dog(Animal):
    def run(self_b):
        print('Dog is running...')

class Cat(Animal):
    def run(self_c):
        print('Cat is running...')

a = Animal()
d = Dog()
c = Cat()












