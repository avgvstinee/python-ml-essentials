
# Changing mutable object with assignment parameter

values = [1,2,3]

def func (values):
    values[1] = 42 # This affects the 'values' argument
    
    values = 'something else'  # This creates a new local variable 'values', does not affect the argument   
    
func(values)
print(values)  # Output: [1, 42, 3]