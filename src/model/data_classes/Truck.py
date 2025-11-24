from .Vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self):
        super().__init__("truck")

    def start_engine(self):
        print("I'm a truck")
