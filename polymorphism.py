implementing samething in different ways.
2 types of polymorphism 1.complie time (method overloading) 2.runtime(Method overriding)

method overloading --- add(), add(a,b), add(a,b,c)  add(a,b,c,d)
python not supporting direct method overloading so we are using default parameters in 

class Demo:
    def add(self,a,b,c=10):
        print(a+b+c)
obj=Demo()
obj.add(100,200)
obj.add(25,23,56)

here c=10 is the default parameter.
----------------------------------------------------

Runtime polymorphism

class Parent:
    def transport(self):
        print("cycle")
class Child(Parent):
    def transport(self):
        print("bike")

c=Child()
c.transport()

here methods should be same in parent and child class then only the method overriding will work here. 
