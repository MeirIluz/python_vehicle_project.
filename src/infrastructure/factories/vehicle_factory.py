from model.data_classes.Vehicle import Vehicle
from model.data_classes.Car import Car
from model.data_classes.Truck import Truck
from model.data_classes.Motorcycle import Motorcycle
from model.data_classes.Plane import Plane


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        vehicle_type = vehicle_type.lower()

        for v in Vehicle.ExistingVehicle:
            if v.__name__.lower() == vehicle_type:
                return v()

        raise ValueError(
            f"Vehicle type '{vehicle_type}' not found, make sure you imported it!")
