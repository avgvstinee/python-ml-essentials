
# variable positional parameters

def minimum(*n):
    # print(n)  # n is a tuple
    if n:  # check if n is not empty
        min_value = n[0]
        for value in n[1:]:
            if value < min_value:
                min_value = value
        print(min_value)

minimum(1, 3, -7, 9)  # n = (1, 3, -7, 9) Output: -7
minimum(8, 3, 5)      # n = (8, 3, 5) Output: 3
minimum()             # n = () Output: nothing      
