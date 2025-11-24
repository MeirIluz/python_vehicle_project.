from .Vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self):
        super().__init__("motorcycle")

    def start_engine(self):
        print("I'm a motorcycle")
