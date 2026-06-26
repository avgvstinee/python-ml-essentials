
class A:
    label = 'a'

class B(A): 
    pass # was : label = 'b'
    
class C(A):
    label = 'c'

class D(B,C):
    pass

d = D()
print(d.label) # Hypothetically this could be either 'b' or 'c
print(d.__class__.mro())
