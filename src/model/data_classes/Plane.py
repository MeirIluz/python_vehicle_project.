from infrastructure.interfaces.ivehicle import IVehicle


class Plane(IVehicle):
    def start_engine(self):
        print("I'm a Plane")
