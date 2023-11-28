
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self,carname):
        self.__carname = carname

    def go(self):
        print(f"You drive the {self.__carname}")

    def stop(self):
        print("This car is stopped")

    # settergetter
    def setcarname(self,newname):
        self.__carname = newname
    def getcarname(self):
        return self.__carname


class Motorcycle(Vehicle):
    def __init__(self,carname):
        self.__carname = carname

    def go(self):
        print(f"You drive the {self.__carname}")

    def stop(self):
        print("This motorcycle is stopped")
    def setcarname(self,newname):
        self.__carname = newname
    def getcarname(self):
        return self.__carname


#vehicle = Vehicle()
car = Car("Mercedes")
motorcycle = Motorcycle("Yamaha")

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()