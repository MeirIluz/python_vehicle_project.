from Vehicle import Vehicle


class Plane(Vehicle):

    def __init__(self):
        super().__init__("Plane")

    def start_engine(self):
        print("I'm a plane")
