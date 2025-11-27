from infrastructure.interfaces.ivehicle import IVehicle


class Motorcycle(IVehicle):
    def start_engine(self):
        print("I'm a Motorcycle")
