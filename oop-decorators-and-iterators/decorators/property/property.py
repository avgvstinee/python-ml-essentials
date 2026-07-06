"""
Property is a way to make a method to behave like an attribute. 
It allows us to define a method that can be accessed like an attribute,
and it can be used to define getter, setter, and deleter methods for an attribute.
"""



class Person :
    def __init__(self,name,age):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError("Age must be within [18,99]")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        
        if name.strip():
            self._name = name
        else:
            raise ValueError("Name cannot be empty")
        


person = Person("Kholofelo", 26)
print(person.name)
print(person.age)

#person.name =  ''
person.age = 100
#print(person.name) # This will raise a ValueError because the name cannot be empty.
print(person.age) # This will raise a ValueError because the age must be within [18,99].