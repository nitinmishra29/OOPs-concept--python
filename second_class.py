# Class method and self
#-------ADD AETHOD TO CAR CLASS TAT DISPLAYS THE FULL NAME OF THE CAR (BRAND AND MODEL)


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def Full_Name(self):
        return f"{self.brand} {self.model}"

tata_car= Car("tata","nexus")
print(tata_car.brand)
print(tata_car.model)
print(tata_car.Full_Name())