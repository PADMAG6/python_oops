class Students:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
    pass
a= Students()
a.name = "padma"
a.marks = 20
did_pass = a.check_pass_fail()
print(did_pass)


---------------------------class-objects--------------------
lass Human:
    def __init__(self,c,h):
        self.color= c
        self.height = h
    def run(self):
        print("Running---")
    def walk(self):
        print("Walk------")

obj = Human('White',4.11)
obj.run()
print(obj.color,obj.height)
obj2 = Human("Red", 3.1)
print(obj2.color,obj2.height)



__________________triangle_perimeter________________--
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        P = self.a + self.b + self.c
        return P

e = Triangle(3,5,6)
print(e.perimeter())

-------------------------inheritance-------------------------
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        
        
        
        
        
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")


class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")
        
        
t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)        

t1.display_info()   #Method overwriting

############method overwirting###########
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        Polygon.display_info(self)


class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

t1.display_info()
        
#################super() function###############3
here super() is the object of Polygon, super is not a class

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        value = 0
        for side in self.sides:
            value += side
        return value


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        # Polygon.display_info(self)
        super().display_info()

class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("Perimeter:", perimeter)

t1.display_info()
