# INHERITANCE 
#------Create an electric class car that inherits from the car class and haas an addtional attribute battery_size


class Car:
    def __init__(self,brand,model):  
        self.brand=brand
        self.model=model

    def Full_Name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
       # super().__init__(brand,model) this also works
        super().__init__(brand,model)         # super for inheriting from above class
        self.battery_size=battery_size

# tata_car= Car("tata","nexus")
# print(tata_car.brand)
# print(tata_car.model)
# print(tata_car.Full_Name())

electric_vehice=ElectricCar("tata","nexa",20)
print(electric_vehice.model)
print(electric_vehice.Full_Name())


