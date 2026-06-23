
def outer(x): # x=5
    def inner(y):  # y=10
        return x + y
    return inner

add_five = outer(5)
result = add_five(10) # inner(10) => 5 + 10 = 15
print(f'x + y : {result}') 
