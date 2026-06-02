# This technique is called decoration

def func(arg1,arg2,...,argN):
    pass

func = decorator(func) # decoration point

# is equivalent to

@decorator
def func(arg1,arg2,....argN):
    pass
# we can also use multiple decorators

def func(arg1,arg2,....,argN):
    pass

func = decorator1(decorator2(func)) # decoration point

@decorator1
@decorator2
def func(arg1,arg2,....,argN):
    pass


# Another syntax for multiple decorators

def func(arg1,arg2,....,argN):
    pass

func = decoarg(arg_a , arg_b) (func)

# is equivalent to the following

@decoarg(arg_a , arg_b)
def func(arg1,arg2,...,argN):
    pass