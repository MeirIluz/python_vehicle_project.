from infrastructure.interfaces.ivehicle_manager import IVehicleManager
from infrastructure.interfaces.ivehicle import IVehicle

from model.data_classes.Car import Car
from model.data_classes.Truck import Truck
from model.data_classes.Motorcycle import Motorcycle


class VehicleManager(IVehicleManager):
    def __init__(self) -> None:
        self._vehicles: list[IVehicle] = [
            Car(),
            Truck(),
            Motorcycle(),
        ]

    def run_all(self) -> None:
        for v in self._vehicles:
            v.start_engine()
