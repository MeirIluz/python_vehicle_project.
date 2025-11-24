from Vehicle import Vehicle
from Car import Car
from Truck import Truck
from Motorcycle import Motorcycle
from Plane import Plane

class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        vehicle_type = vehicle_type.lower()

        for v in Vehicle.ExistingVehicle:
            if v.__name__.lower() == vehicle_type:
                return v()  

        raise ValueError(f"Vehicle type '{vehicle_type}' not found, make sure you imported it!")

