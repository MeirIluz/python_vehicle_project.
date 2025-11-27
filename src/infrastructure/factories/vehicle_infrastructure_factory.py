from model.data_classes.Car import Car
from model.data_classes.Motorcycle import Motorcycle
from model.data_classes.Truck import Truck
from model.data_classes.Plane import Plane

class VehicleInfrastructureFactory:
    @staticmethod
    def create_car() -> Car:
        return Car()

    @staticmethod
    def create_motorcycle() -> Motorcycle:
        return Motorcycle()

    @staticmethod
    def create_truck() -> Truck:
        return Truck()
    
    @staticmethod
    def create_plane() -> Plane:
         return Plane()