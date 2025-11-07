
# shorter version of return.single.value.py

from functools import reduce
from operator import mul

def factorial(number):
    return reduce(mul, range(1, number + 1), 1)

f = factorial(5)
print(f)  # Output: 120
    
