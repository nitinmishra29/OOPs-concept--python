#Class Variable
#---------- add a class variable in car that keeps track of the no of cars created


class Car:
    total_car = 0

    def __init__(self,brand,model):  
        self.__brand=brand    # if we use '__' under score time befor attribute its become private
        self.model=model
        Car.total_car += 1    # we can use Car.total_car to acces this

# self.total_car += 1   ----------we can use self.total_car as well above line   --------

    def get_brand(self):
        return self.__brand + '!'

    def Full_Name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
       # super().__init__(brand,model) this also works
        super().__init__(brand,model)         # super for inheriting from above class
        self.battery_size=battery_size


    def fuel_type(self):
        return "electric charging"

tata_car= Car("tata","nexus")
tata_car2 = Car("tata","safari")
print(Car.total_car)
print(tata_car.total_car)



electric_vehice=ElectricCar("tata","nexa",20)
print(Car.total_car)

