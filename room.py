class Room:
    def __init__(self, room_id, room_type, price, status="Available"):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.status = status

    def change_status(self, new_status):
        self.status = new_status
        return f"Room {self.room_id} status changed to {self.status}."

    def get_details(self):
        return f"Room {self.room_id} ({self.room_type}): {self.price} USD per night - Status: {self.status}"
