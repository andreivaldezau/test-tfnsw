class Train:
    def __init__(self, entity_id: str) -> None:
        self.entity_id = entity_id
        self.trip_id: str = ""
        self.route_id: str = ""
        self.schedule_relationship = None
        self.vehicle_id: str = ""
        self.vehicle_label: str = ""
        # self.vehicle_model
        self.latitude = 0
        self.longitude = 0
        self.stop_id = ""
        # self.timestamp = 0
        self.congestion_level = None
        self.occupancy_status = None

    def get_train_data(self, entity):
        self.trip_id = entity.vehicle.trip.trip_id
        self.route_id = entity.vehicle.trip.route_id
        self.schedule_relationship = entity.vehicle.trip.schedule_relationship
        self.vehicle_id = entity.vehicle.vehicle.id
        self.vehicle_label = entity.vehicle.vehicle.label
        # self.vehicle_model
        self.latitude = entity.vehicle.position.latitude
        self.longitude = entity.vehicle.position.longitude
        self.stop_id = entity.vehicle.stop_id
        # self.timestamp = entity.vehicle.timestamp
        self.congestion_level = entity.vehicle.congestion_level
        self.occupancy_status = entity.vehicle.occupancy_status
