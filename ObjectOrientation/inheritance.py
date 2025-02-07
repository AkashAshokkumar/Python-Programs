# Single Inheritance
class demo:
    def disp1(self):
        print('Inside demo classs')

class demo1(demo):
    pass

d1 = demo1()
d1.disp1()
print('--------------------------------------')
# Hieracical Inheritance

class parent():
    def meth1(self):
        print('Inside parent class')

class Child1(parent):
    def meth2(self):
        print("Inside Child class")

class Child2(parent):
    pass

c1 = Child1()
c1.meth1()
c1.meth2()
print('--------------------------------------')

# MultiLevel Inheritance

class Parent1:
    def me(self):
        print('Inside Parent1 class')

class Childd1(Parent1):
    def me1(self):
        print("Inside Child class")

class Childd2(Childd1):
    pass

child = Childd2()
child.me()
child.me1()
print('--------------------------------------')
