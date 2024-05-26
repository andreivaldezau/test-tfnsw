class Train:
    def __init__(self, entity) -> None:
        self.entity_id: str = entity.id
        self.trip_id: str = entity.vehicle.trip.trip_id
        self.route_id: str = entity.vehicle.trip.route_id
        self.schedule_relationship = entity.vehicle.trip.schedule_relationship
        self.vehicle_id: str = entity.vehicle.vehicle.id
        self.vehicle_label: str = entity.vehicle.vehicle.label
        # self.vehicle_model
        self.latitude = entity.vehicle.position.latitude
        self.longitude = entity.vehicle.position.longitude
        self.stop_id: str = entity.vehicle.stop_id
        # self.timestamp = 0
        self.congestion_level = entity.vehicle.congestion_level
        self.occupancy_status = entity.vehicle.occupancy_status
