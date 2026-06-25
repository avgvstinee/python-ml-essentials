
from class_inheritance import Car, CityCar, RaceCar, F1Car

car = Car()
racecar = RaceCar()
f1car = F1Car()

cars = [(car, 'car'), (racecar, 'racecar'), 
        (f1car, 'f1-car')]

car_classes = [Car, RaceCar, F1Car]

for car, car_name in cars:
    for class_ in car_classes:
        belongs = isinstance(car, class_)
        msg = 'is a ' if belongs else 'is not a '
        print(car_name, msg,class_.__name__)

""" Prints:
car is a Car
car is not a RaceCar
car is not a F1Car

racecar is a Car
racecar is a RaceCar
racecar is not a F1Car

f1-car is a Car
f1-car is RaceCar
f1-car is a F1Car
"""