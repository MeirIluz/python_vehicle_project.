from infrastructure.interfaces.ivehicle import IVehicle
from infrastructure.factories.logger_factory import LoggerFactory
from globals.consts.const_strings import ConstStrings
from globals.consts.logger_messages import LoggerMessages


class Motorcycle(IVehicle):
    def __init__(self):
        self._logger = LoggerFactory.get_logger_manager()

    def start_engine(self):
        vehicle_name = self.__class__.__name__
        
        self._logger.log(
            ConstStrings.LOG_NAME_DEBUG,
            LoggerMessages.VEHICLE_ENGINE_MESSAGE.format(vehicle_name)
        )