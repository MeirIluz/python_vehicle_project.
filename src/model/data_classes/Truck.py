from infrastructure.interfaces.ivehicle import IVehicle


class Truck(IVehicle):
    def start_engine(self):
        print("I'm a Truck")
