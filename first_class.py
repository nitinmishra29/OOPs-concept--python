# Basic class and object
#---- CReate a class car with attribute like brand and model. THEN CREAtE A INSTANCES OF THIs CLASS

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

tata_car= Car("tata","nexus")
print(tata_car.brand)
print(tata_car.model)