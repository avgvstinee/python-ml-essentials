
class Engine:
    def start(self):
        pass
    def stop(self):
        pass

class ElectricEngine(Engine): # ElectricEngine inherits from Engine ( IS-A relationship )
    pass

class V8Engine(Engine): # V8Engine inherits from Engine ( IS-A relationship )
    pass


class Car :
    engine_cls = Engine # class attribute (shared by all instances of Car)
    
    def __init__(self):
        self.engine = self.engine_cls() # instance attribute (unique to each instance of Car)
    
    def start(self):
        print('Starting engine {0} for car {1}.....Wroom, Wroom!'
              .format(
                  self.engine.__class__.__name__, # Engine class name
                  self.__class__.__name__) # Car class name
            )
        self.engine.start() # call start method of the engine instance
    
    def stop(self):
        self.engine.stop() # call stop method of the engine instance
    
class RaceCar(Car):
    engine_cls = V8Engine

class CityCar(Car):
    engine_cls = ElectricEngine

class F1Car(Car):
    engine_cls = V8Engine
    

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()

cars = [car, racecar, citycar, f1car]

for car in cars:
    car.start()