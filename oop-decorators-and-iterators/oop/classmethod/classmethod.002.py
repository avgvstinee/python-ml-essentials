

class Student:
    name = 'unknown' # class attribute
    
    def __init__(self):
        self.age = 20  # instance attribute
    
    @classmethod        # class decorator
    def tostring(cls):  # cls is the first parameter, which is used to access the class attribute
        print('Student Class Attributes: name=',cls.name, ', age=', cls.age)


Student.tostring()

"""
The class method can only access class attributes, but not the instance attributes. 
It will raise an error if trying to access the instance attribute in the class method
"""