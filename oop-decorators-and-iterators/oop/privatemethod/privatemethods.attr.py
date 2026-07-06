""""
A very common use case for private attributes is helper methods that are supposed to be used by public ones
(possibly in call chains in conjunction with other methods), and internal data,
such as scaling factors, or any other data that we would ideally put in a constant 
(a variable that cannot change, but, surprise, surprise, Python doesn't have those either).


"""


class A:
    def __init__(self,factor):
        self._factor = factor
    def op1(self):
        print('Op1 with factor {}...'.format(self._factor))
        
    
class B(A):
    def op2(self,factor):
        self._factor = factor
        print('Op1 with factor {}...'.format(self._factor))
    

obj = B(100)
obj.op1() # 100
obj.op2(42) # 42
obj.op1() # 42 <-- This is a problem, because the factor has changed, and we don't want that to happen.
print(obj.__dict__.keys()) # dict_keys(['_factor'])