from abc import ABC, abstractmethod


class Vehicle(ABC):

    ExistingVehicle = []

    def __init_subclass__(cls):
        Vehicle.ExistingVehicle.append(cls)


    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    @abstractmethod
    def start_engine(self):
        pass
