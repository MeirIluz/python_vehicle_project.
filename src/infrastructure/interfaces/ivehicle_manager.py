from abc import ABC, abstractmethod


class IVehicleManager(ABC):
    @abstractmethod
    def run_all(self) -> None:
        pass
