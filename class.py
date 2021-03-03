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
