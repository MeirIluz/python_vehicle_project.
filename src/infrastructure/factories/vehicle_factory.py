from model.vehicles.Vehicle import Vehicle
from model.vehicles.Car import Car
from model.vehicles.Truck import Truck
from model.vehicles.Motorcycle import Motorcycle
from model.vehicles.Plane import Plane


class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type):
        vehicle_type = vehicle_type.lower()

        for v in Vehicle.ExistingVehicle:
            if v.__name__.lower() == vehicle_type:
                return v()

        raise ValueError(
            f"Vehicle type '{vehicle_type}' not found, make sure you imported it!")
