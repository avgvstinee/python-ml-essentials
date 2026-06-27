
class Student:
    name = 'unknown' # class attribute
    
    def __init__(self):
        self.age = 20  # instance attribute
    
    @classmethod        # class decorator
    def tostring(cls):  # cls is the first parameter, which is used to access the class attribute
        print('Student Class Attributes: name=',cls.name)


Student.tostring()