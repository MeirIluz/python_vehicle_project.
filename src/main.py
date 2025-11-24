from VehicleFactory import VehicleFactory


def main():
    factory = VehicleFactory()

    v1 = factory.create_vehicle("car")
    v2 = factory.create_vehicle("truck")
    v3 = factory.create_vehicle("motorcycle")
    v4 = factory.create_vehicle("plane")

    v1.start_engine()
    v2.start_engine()
    v3.start_engine()
    v4.start_engine()


if __name__ == "__main__":
    main()
