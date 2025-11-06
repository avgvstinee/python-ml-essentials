
# variable keyword parameters (**args)

def func(**kwargs):
    print(kwargs)  # kwargs is a dictionary

func(a=1, b=2)  # kwargs = {'a': 1, 'b': 2} Output: {'a': 1, 'b': 2
func() # kwargs = {} Output: {}
func(name="Alice", age=30, city="New York") # kwargs = {'name': 'Alice', 'age': 30, 'city': 'New York'} Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}    

