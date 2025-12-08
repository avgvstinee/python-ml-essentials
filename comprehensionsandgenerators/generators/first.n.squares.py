# Generators

# Classical function approach
def get_squares(n):
    return [ x ** 2  for x in range(n)]

print(get_squares(10))

# Generator function approach
def get_squares_gen(n):
    for x in range(n):
    # we yield , we dont return  
        yield x ** 2
        
print(list(get_squares_gen(10)))

