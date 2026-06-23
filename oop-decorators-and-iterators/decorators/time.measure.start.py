from time import time , sleep

def f():
    sleep(.3)

def g():
    sleep(.5)
    
# measure time taken by f and g
t = time()
# ------call------
f()
print('f took', time() - t) # f took 0.3050727844238281

t = time()
# -----call------
g()
print('g took', time() - t) # g took 0.5009047985076904