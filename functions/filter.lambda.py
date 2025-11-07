
# Anonymous function -> lambda function

def get_multiple_of_five(number):
    return list(filter(lambda k: not k % 5 , range(number)))

print(get_multiple_of_five(30))  # prints [0, 5, 10, 15, 20, 25]