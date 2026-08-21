
class Weird:
    def __init__(self,s):
        self.s = s
    
    def __len__(self):
        return len(self.s)
    
    def __bool__(self):
        return '42' in self.s
    


weird = Weird('Hello! I am 9 years old!')
print(len(weird))  # Output: 24
print(bool(weird))  # Output: False

weird2 = Weird('Hello! I am 42 years old!')
print(len(weird2))  # Output: 24
print(bool(weird2))  # Output: True
