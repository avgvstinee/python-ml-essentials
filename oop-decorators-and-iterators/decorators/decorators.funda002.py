
def make_pretty(func): # function as argument
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
    
ordinary() # ordinary() => inner() => I got decorated \n I am ordinary