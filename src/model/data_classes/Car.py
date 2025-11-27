from infrastructure.interfaces.ivehicle import IVehicle


class Car(IVehicle):
    def start_engine(self):
        print("I'm a Car")
