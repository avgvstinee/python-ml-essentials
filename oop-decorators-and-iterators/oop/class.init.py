
class Rectangle : 
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def area(self):
        return self.side_a * self.side_b

r1 = Rectangle(10,4) 
print(f'Side A : {r1.side_a},  Side B : {r1.side_b}') # 10,  4
print(f'The result : {r1.area()}') # 40


r2 = Rectangle(5, 6) 
print(f'Side A : {r2.side_a},  Side B : {r2.side_b}') # 5,  6
print(f'The result : {r2.area()}') # 30