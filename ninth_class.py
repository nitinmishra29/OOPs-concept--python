# Class inheritence and isinstance() function
#-- Demonstrate the use of isinstance() to check if electric_vehice is an instance of car and electric car

class Car:
    total_car = 0

    def __init__(self,brand,model):  
        self.__brand=brand    # if we use '__' under score time befor attribute its become private
        self.__model=model  # because we dont want to acces it by anone to change this
        Car.total_car += 1    # we can use Car.total_car to acces this

# self.total_car += 1   ----------we can use self.total_car as well above line   --------

    def get_brand(self):
        return self.__brand + '!'

    def Full_Name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @property           # to hide this property from this it can be accesa s a attribute
    def model(self):
        return self.__model
    

    # this decorator helpt to make the car_description function accessible ny only class Car not other insance can acces it like total_car
    @staticmethod            # this is a decorator which is sused for incresasing the fun of method or security
    def car_description():
        return "car is a metal body"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
       # super().__init__(brand,model) this also works
        super().__init__(brand,model)         # super for inheriting from above class
        self.battery_size=battery_size


    def fuel_type(self):
        return "electric charging"

tata_car= Car("tata","nexus")
tata_car2 = Car("tata","safari")

#tata_car.model = "city"  after property decorator it cant be assign city
#print(tata_car.model)


electric_vehice=ElectricCar("tata","nexa",20)
print(isinstance(electric_vehice,ElectricCar)) # its tels wheather itstrue or not electric_vehice is instance of ElementCar ornot same for other
print(isinstance(electric_vehice,Car))