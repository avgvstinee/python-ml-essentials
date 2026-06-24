
class Point :
    x = 10
    y = 7
    
# instance of Point
p = Point()
print(p.x) # 10 (inherited)
print(p.y) # 7 (inherited)

p.x = 12 # shadowing the class attribute x
print(p.x) # 12 (instance attribute)
print(Point.x) # 10 (class attribute remains unchanged)

del p.x # delete the instance attribute x
print(p.x) # 10 (inherited again from the class attribute)

p.z = 3 # dynamically add a new attribute to the instance
print(p.z) # 3 (instance attribute)
print(Point.z) # AttributeError: type object 'Point' has no attribute 'z'