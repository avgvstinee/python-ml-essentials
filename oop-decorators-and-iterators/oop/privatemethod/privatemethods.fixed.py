""""
A very common use case for private attributes is helper methods that are supposed to be used by public ones
(possibly in call chains in conjunction with other methods), and internal data,
such as scaling factors, or any other data that we would ideally put in a constant 
(a variable that cannot change, but, surprise, surprise, Python doesn't have those either).

Name mangling means that any attribute name that has at least two leading underscores and at most one trailing underscore,
such as __my_attr, is replaced with a name that includes an underscore and the class name before the actual name,
such as _ClassName__my_attr.
This means that when you inherit from a class, 
the mangling mechanism gives your private attribute two different names in the base and child classes so that name collision is avoided. 
Every class and instance object stores references to their attributes in a special attribute called __dict__, 
so let's inspect obj.__dict__ to see name mangling in action:

"""


class A:
    def __init__(self,factor):
        self.__factor = factor
    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))
        
    
class B(A):
    def op2(self,factor):
        self.__factor = factor
        print('Op1 with factor {}...'.format(self.__factor))
    

obj = B(100)
obj.op1() # 100
obj.op2(42) # 42
obj.op1() # 100 <-- This is the expected behavior, as the factor is private and cannot be changed from outside the class.
print(obj.__dict__.keys()) # dict_keys(['_A__factor'])