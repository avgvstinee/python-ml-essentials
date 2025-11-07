
# factorial 

def factorial(number):
    if number in(0,1):
        return 1
    result = number
    
    for value in range(2,number):
        result *= value
    return result

f = factorial(5)
print(f)  # Output: 120
     