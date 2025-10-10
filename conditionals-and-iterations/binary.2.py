# a better version of binary.py , clean and pythonic

n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)  # divmod returns the quotient and remainder
    remainders.append(remainder)  # we keep track of the remainders
remainders.reverse()  # The binary representation is the reverse of the remainders
print(remainders)  # Output: [1, 0, 0, 1, 1]