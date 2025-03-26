class GuestServices:
    def __init__(self, service_id, service_type):
        self.service_id = service_id
        self.service_type = service_type
        self.status = "Pending"

    def request_service(self):
        self.status = "In Progress"
        return f"Service {self.service_type} requested, status: {self.status}."

    def track_status(self):
        return f"Service {self.service_type} is currently {self.status}."
