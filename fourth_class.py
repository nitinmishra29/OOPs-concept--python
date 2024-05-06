# Encapsulation
#-------------- modify the car class to encapsulate the brand attribute,making it private, provide a getter method for it



class Car:
    def __init__(self,brand,model):  
        self.__brand=brand  # if we use '__' under score time befor attribute its become private
        self.model=model
    
    def get_brand(self):
        return self.__brand + '!'

    def Full_Name(self):
        return f"{self.__brand} {self.model}"
    

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
#print(electric_vehice.model)
#print(electric_vehice.Full_Name())
#print(electric_vehice.brand)          after comment out the next line working becaouse of getter
print(electric_vehice.get_brand())


