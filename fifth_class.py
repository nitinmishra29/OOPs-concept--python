#Polymorphism
#------------- demonstrate polymorphism ny defining a method fuel_type in both CAR and ElectricCar but with different behaviors



class Car:
    def __init__(self,brand,model):  
        self.__brand=brand  # if we use '__' under score time befor attribute its become private
        self.model=model
    
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

print(tata_car.fuel_type())  # this print the Car cass batteryy

electric_vehice=ElectricCar("tata","nexa",20)

print(electric_vehice.fuel_type())




