
# lst method 
square = []

for n in range(10):
    square.append(n ** 2)
    
print(square)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2nd method 

squares = list(map(lambda x: x ** 2, range(10)))
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# comprehensions
squares_comprehension = [n**2 for n in range(10)]
print(squares_comprehension)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

