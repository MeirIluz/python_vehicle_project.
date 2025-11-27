from infrastructure.interfaces.ivehicle_manager import IVehicleManager
from infrastructure.interfaces.ivehicle import IVehicle
import model.data_classes.Car as Car
import model.data_classes.Truck as Truck
import model.data_classes.Motorcycle as Motorcycle

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
