
class Simplest(): # when empty , the brace are optional
    pass

print(type(Simplest)) # <class 'type'> , what type is this Object? 
simp = Simplest() # create an instance of the class of simplest : simp

print(type(simp)) # what type is simp ?
# is simp an instance of Simplest ?

print(type(simp) is Simplest) # There's a better way to do this.