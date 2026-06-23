from time import time, sleep

def f():
    sleep(.3)

def g():
    sleep(.5)

# measure time taken by f and g
def measure(func):
    t=time()
    func()
    # print time taken
    print(func.__name__, 'took', time() - t)

measure(f) # f took 0.3050727844238281
measure(g) # g took 0.5009047985076904