from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
    def fuel_type(self):
        pass 
class Car(Vehicle): 
       def start(self):
           print("car started")
       def stop(self):
           print("car stopped")
       def fuel_type(self):
           print("Petrol")

class Bike(Vehicle): 
       def start(self):
           print("bike started")
       def stop(self):
           print("bike stopped")
       def fuel_type(self):
           print("Petrol")

class Tesla(Vehicle): 
       def start(self):
           print("tesla started")
       def stop(self):
           print("tesla stopped")
       def fuel_type(self):
           print("electric")
print("=>Car Details")
my_car = Car() 
my_car.start()
my_car.stop()
my_car.fuel_type()


print("=>Bike Details")
my_bike = Bike() 
my_bike.start()
my_bike.stop()
my_bike.fuel_type()

print("=>Tesla Details")
my_tesla = Tesla()
my_tesla.start()
my_tesla.stop()
my_tesla.fuel_type()
 
