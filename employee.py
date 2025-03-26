class Employee:
    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role

    def manage_reservations(self):
        return f"Employee {self.name} ({self.role}) is managing reservations."

    def assist_guests(self):
        return f"Employee {self.name} is assisting guests."
