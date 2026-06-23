
class Person :
    species = 'Human'

print(Person.species) # Human
Person.alive = True # dynamically add a new attribute to the class
print(Person.alive) # True

man = Person() # create an instance of the class Person
print(man.species) # Human (inherited)
print(man.alive) # True (inherited)
Person.alive = False # change the class attribute

print(man.alive) # False (inherited)
man.name = 'Augustine'
man.surname = 'Ramafalo'

print(man.name, man.surname)