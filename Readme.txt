Royal Inn Suite: Hotel Management System  

Royal Inn Suite is an advanced hotel management system designed for **guest reservations, room management, secure payments, and additional hotel services**. Built using **Object-Oriented Programming (OOP)** principles, it ensures modularity and scalability.  

Features  
- Guest registration & booking management  
- Room availability & reservations  
- Secure payment processing & invoices  
- Booking cancellations & modifications  
- Guest service requests (housekeeping, transport)  
- Automated notifications  

Installation  
Prerequisites  
Ensure **Python 3.8+** is installed:  
python --version
Clone the Repository
git clone https://github.com/yourusername/RoyalInnSuite.git
cd RoyalInnSuite
Run the Application
python guest.py
python room.py
python reservation.py
python payment.py
python guest_services.py
Running Tests
Run all tests:
python -m unittest -v test_hotel.py
Run individual tests:
python -m unittest test_hotel.TestHotelManagement.test_guest_creation -v
python -m unittest test_hotel.TestHotelManagement.test_room_status_change -v
Project Structure
RoyalInnSuite/
│── guest.py               # Manages guest accounts
│── room.py                # Handles room details & availability
│── reservation.py         # Manages bookings & cancellations
│── payment.py             # Processes payments & invoices
│── guest_services.py      # Handles additional hotel services
│── test_hotel.py          # Unit tests
│── README.md              # Documentation
└── UML-diagram.png        # System architecture diagram
GitHub Repository
Ensure your latest code is pushed with a clear commit history including:
•	All source code & test files
•	UML diagrams & documentation
•	Screenshots of test results
License
This project is licensed under the MIT License.

