from infrastructure.factories.vehicle_factory import VehicleFactory


def main():

    v1 = VehicleFactory.create_vehicle("car")
    v2 = VehicleFactory.create_vehicle("truck")
    v3 = VehicleFactory.create_vehicle("motorcycle")
    v4 = VehicleFactory.create_vehicle("plane")

    v1.start_engine()
    v2.start_engine()
    v3.start_engine()
    v4.start_engine()


if __name__ == "__main__":
    main()
