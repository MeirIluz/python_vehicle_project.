from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        super().__init__("car")

    def start_engine(self):
        print("I'm a car")
