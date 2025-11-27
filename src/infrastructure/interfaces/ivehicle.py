from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    