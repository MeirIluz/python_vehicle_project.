from infrastructure.factories.vehicle_infrastructure_factory import VehicleInfrastructureFactory


class VehicleFactory:
    @staticmethod
    def create_all():
        vehicles = [
            VehicleInfrastructureFactory.create_car(),
            VehicleInfrastructureFactory.create_motorcycle(),
            VehicleInfrastructureFactory.create_truck()
        ]

        for v in vehicles:
            v.start_engine()
