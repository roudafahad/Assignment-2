class Guest:
    def __init__(self, guest_id, name, email, phone, loyalty_points=0):
        self.guest_id = guest_id
        self.name = name
        self.email = email
        self.phone = phone
        self.loyalty_points = loyalty_points

    def view_details(self):
        return f"Guest ID: {self.guest_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Loyalty Points: {self.loyalty_points}"

    def update_contact_info(self, new_email, new_phone):
        self.email = new_email
        self.phone = new_phone
        return "Contact info updated successfully."
