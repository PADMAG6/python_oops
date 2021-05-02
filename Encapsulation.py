public--- with in the class, outside class


private--- with in the class only.

class Demo:
    __a= 10          #private variable
    b= 20
    def __display(self):      #private Method
        print(self.__a)
        print("hellow")
    def show(self):         #show is the public method
        self.__display()

obj=Demo()
#obj.__a     #__a private varible show output wn't shown
print(obj.b)  #b is public variable
#obj.show()
