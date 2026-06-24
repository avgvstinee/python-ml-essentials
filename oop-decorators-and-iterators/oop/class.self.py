
class Square:
    side = 8
    def area(self): # self is a reference to the instance of the class
        return self.side ** 2

sq = Square()
print(sq.area())
print(Square.area(sq)) # equivalent to sq.area()

sq.side = 10 # shadowing the class attribute side
print(sq.area()) # 100 (instance attribute is used)