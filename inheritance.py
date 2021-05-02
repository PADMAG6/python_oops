parent-child relation.
base class-derived class

--------------Single Inheritance-------------------------
//one base class, one derivered class

class BaseClass:
    a=10                        #parentt class
    b=20
    def display(self):
        print("base class")
        
class DerivedClass(BaseClass):           #child class
    c=20
    d=100
    def show(self):
        print("Derived class")

obj = BaseClass()
obj1 = DerivedClass()

print(obj1.a)


// Inheritance is 3 types    1.single 2.Multilevel 3.Hierarchical 4.Multiple 

---------------------Multilevel Inheritance---------------------

// one base class, one or more derived classes.

class GrandParent:
    def gwalk(self):
        print("I am old i can not run")
class Parent(GrandParent):
    def pwalk(self):
        print("I can walk myself")
class Child(Parent):
    def cwalk(self):
        print("I amm young i can walk")

obj = Child()
obj.gwalk()
obj.cwalk()
obj.pwalk()

------------------------------Hierarchical Inheritance-----------------
//one base class , two child class 

class Parent:
    def pdisplay(self):
        print("i am parent class")
class Child1(Parent):
    def c1display(self):
        print("I am child1 class")
class Child2(Parent):
    def c2display(self):
        print("I am child 2 class")

p=Child2()
p.c2display()
p.pdisplay()

-------------------------------Multiple Inheritance-----------------------
//one or two base classes, one child class

class Father:
    def fdisplay(self):
        print("father class")
class Mother:
    def mdisplay(self):
        print("Mother class")
class Child(Father,Mother):
    def cdisplay(self):
        print("child from mother and father class")


c= Child()
c.mdisplay()
c.fdisplay()
m=Mother()
m.mdisplay()









        
