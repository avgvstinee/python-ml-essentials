
def print_squares(start,end):
    yield from (n ** 2 for n in range(start,end))

for n in print_squares(2,5):
    print(n)
# prints:
# 4
# 9
# 16
