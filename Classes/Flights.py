import os
from .Base import TravelService

class Flight(TravelService):
    FILE_PATH = "Database2/flights2.txt"

    def __init__(self, service_id, availability, price, service_name, departure, destination, date):
        super().__init__(service_id, availability, price, service_name)
        self.departure = departure
        self.destination = destination
        self.date = date

        self.save_to_file()
    
    def calculate_cost(self, no_of_seats):
        """Calculate the total cost based on the number of seats booked."""
        return self.get_price() * no_of_seats
    
    def book_service(self, no_of_seats):
        """Book flight seats if available and update the file."""
        if self.get_avilability() >= no_of_seats:
            self.set_avilability(self.get_avilability() - no_of_seats)
            self.update_flight_file()
            print(f"Booking successful! {no_of_seats} seats booked.")
            return True
        print("Booking failed: Not enough available seats!")
        return False
    
    def get_details(self):
        """Return flight details as a dictionary."""
        return {
            "service_id": self.get_service_id(),
            "service_name": self.get_service_name(),
            "departure": self.departure,
            "destination": self.destination,
            "date": self.date,
            "availability": self.get_avilability(),
            "price": self.get_price()
        }

    @classmethod
    def load_flights(cls):
        """Load flights from the database."""
        try:
            with open(cls.FILE_PATH, "r") as file:
                content = file.read().strip()
                return eval(content) if content else [] 
        except Exception:
            print("Error reading flight data.")
            return []

    def save_to_file(self):
        """Append flight details to database."""
        flights = self.load_flights()
        existing_flights = [f for f in flights if f["service_id"] != self.get_service_id()]  # Remove old record
        existing_flights.append(self.get_details()) # Add new flight

        with open(self.FILE_PATH, "w") as file:
            file.write(str(existing_flights))  # Store as a string

        print("Flight details saved successfully!")
        
    def update_flight_file(self):
        """Update flight availability in flights2.txt."""
        flights = Flight.load_flights()
        updated_flights = []

        for flight in flights:
            if flight["service_id"] == self.get_service_id():
                flight["availability"] = self.get_avilability()  # Update availability
            updated_flights.append(flight)  # Add flight (updated or not)

        with open(self.FILE_PATH, "w") as file:
            file.write(str(updated_flights))  # Save without duplication

        print("Flight details updated successfully!")


