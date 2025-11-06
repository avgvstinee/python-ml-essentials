
# Changing a mutable Object 

values = [1,2,3]

def func (values):
    values[1] = 42 # This affects the 'values' argument 

func(values)
print(values)  # Output: [1, 42, 3]