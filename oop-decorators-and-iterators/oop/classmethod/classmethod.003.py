
# The class method can also be used as a factory method to get an object of the class

class Student:
    def __init__(self,name,age):
        self.name = name # instance attribute
        self.age = age # instance attribute
        
    
    @classmethod
    def getobject(cls):
        return cls('Steve',25)
        
std = Student.getobject()
print(std.name)
print(std.age)