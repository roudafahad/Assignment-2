class Reservation:
    def __init__(self, reservation_id, guest, room, check_in, check_out):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.status = "Pending"

    def confirm_reservation(self):
        self.status = "Confirmed"
        self.room.change_status("Booked")
        return f"Reservation {self.reservation_id} confirmed for {self.guest.name}."

    def cancel_reservation(self):
        self.status = "Cancelled"
        self.room.change_status("Available")
        return f"Reservation {self.reservation_id} cancelled for {self.guest.name}."
