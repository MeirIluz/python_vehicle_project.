from model.managers.vehicle_manager import VehicleManager
from infrastructure.interfaces.ivehicle_manager import IVehicleManager


class VehicleFactory:
    @staticmethod
    def create_all() -> None:
        manager: IVehicleManager = VehicleManager()
        manager.run_all()
