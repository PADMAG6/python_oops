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
