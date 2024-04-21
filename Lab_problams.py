                   #Partial function 
     #for squre                
# from functools import partial
# def square(base, exponent):
#     b=base**exponent
#     return b
# squre = partial(square,exponent=2)
# print(squre(5))

# from functools import partial
# # def square(base, exponent):
# #     b=base**exponent
# #     return b
# squre = partial(lambda base,exponent:base**exponent,exponent=2)
# print(squre(5))

# from functools import partial
# squre = partial(lambda num,fix:num if num%fix==0 else "",fix=2)
# for i in range(50):
#     print(squre(i))

#   lambda function for even numbers
# from functools import partial
# even = partial(lambda num,fix:[i for i in range(1,num)if i%fix==0],fix=2)
# print(even(50))


    # Lecture no 9 facade and Singleton patterns
class Sensor(object):

    def __init__(self):
        ...

    def sensor_on(self):
        print("Sensor on")
    
    def sensor_off(self):
        print("Sensor off")

class Smoke(object):

    def __init__(self):
        ...

    def smoke_on(self):
        print("Smoke on")
    
    def smoke_off(self):
        print("Smoke off")

class Lights(object):

    def __init__(self):
        ...

    def light_on(self):
        print("Lights on")

    def light_off(self):
        print("Light off")

class Facade(object):

    """ Facade Design Patterns """

    def __init__(self) -> None:
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Lights()
    
    def emergency(self): 
        self._sensor.sensor_on()
        self._light.light_on()
        self._smoke.smoke_on()

    def no_emergency(self):
        self._sensor.sensor_off()
        self._light.light_off()
        self._smoke.smoke_off()


class SingletonFacade(Facade):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SingletonFacade, cls).__new__(cls)
        return cls.instance
    
if __name__ == "__main__":
    
    facade = SingletonFacade()
    facade2 = SingletonFacade()
    sensor = 35
    print(facade is facade2)
    if sensor > 30:
        facade.emergency()
    else:
        facade.no_emergency() 