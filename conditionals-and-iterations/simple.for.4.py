# What if you wanted to print the position as well, though?
# Should you go back to range(len()) form ? No , you can just use enumerate() built-in function

surnames = ['smith','brown','lamar','palmer','musk','jobs']

for position , surname in enumerate(surnames):
    print(position,surname)