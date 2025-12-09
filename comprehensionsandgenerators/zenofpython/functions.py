
# gcd () function that uses Euclid's algorithm
def gcd(a, b):
    """calculate thr Greatest Common Divisor of a and b""" 
    
    while b != 0:
        a, b = b, a % b
    return a

