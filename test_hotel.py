import unittest
from guest import Guest
from employee import Employee
from room import Room
from reservation import Reservation
from payment import Payment
from guest_services import GuestServices

class TestHotelManagement(unittest.TestCase):

    def test_guest_creation(self):
        print("\n[TEST] Guest Creation")
        guest = Guest(1, "Alice Brown", "alice@example.com", "9876543210")
        expected_output = f"Guest ID: 1, Name: Alice Brown, Email: alice@example.com, Phone: 9876543210, Loyalty Points: 0"
        actual_output = guest.view_details()
        print(f"Expected: {expected_output}\nActual: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_employee_assistance(self):
        print("\n[TEST] Employee Assistance")
        employee = Employee(101, "John Doe", "Manager")
        expected_output = "Employee John Doe is assisting guests."
        actual_output = employee.assist_guests()
        print(f"Expected: {expected_output}\nActual: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_room_status_change(self):
        print("\n[TEST] Room Status Change")
        room = Room(205, "Deluxe", 150)
        expected_output = "Room 205 status changed to Booked."
        actual_output = room.change_status("Booked")
        print(f"Expected: {expected_output}\nActual: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_make_reservation(self):
        print("\n[TEST] Room Reservation")
        guest = Guest(2, "Bob Smith", "bob@example.com", "1234567890")
        room = Room(101, "Suite", 200)
        reservation = Reservation(301, guest, room, "2025-04-01", "2025-04-05")
        expected_output = "Reservation 301 confirmed for Bob Smith."
        actual_output = reservation.confirm_reservation()
        print(f"Expected: {expected_output}\nActual: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_payment_processing(self):
        print("\n[TEST] Payment Processing")
        payment = Payment(501, 400, "Credit Card")
        expected_output = "Transaction 501: 400 USD processed via Credit Card."
        actual_output = payment.process_transaction()
        print(f"Expected: {expected_output}\nActual: {actual_output}")
        self.assertEqual(actual_output, expected_output)

    def test_service_request(self):
        print("\n[TEST] Guest Service Request")
        service = GuestServices(701, "Room Cleaning")
        expected_output = "Service Room Cleaning requested, status: In Progress."
        actual_output = service.request_service()
        print(f"Expected: {expected_output}\nActual: {actual_output}")
        self.assertEqual(actual_output, expected_output)

if __name__ == "__main__":
    unittest.main()
