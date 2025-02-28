import tkinter as tk
from tkinter import ttk, messagebox

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.Flights import Flight 

CURR_USER = None
CALLBACK_FUNCTION = None

# To clear existing widgets
def clear_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def find_flight(root, curr_user, callback_function=None): 
    global CURR_USER, CALLBACK_FUNCTION
    CURR_USER = curr_user
    if callback_function:  # Only update CALLBACK_FUNCTION if it's not None
        CALLBACK_FUNCTION = callback_function

    clear_widgets(root)
    tk.Label(root, text="Searching flights...", font=("Arial", 14)).pack(pady=10)
    
    flights = Flight.load_flights()
    locations = sorted(set(f["departure"] for f in flights) | set(f["destination"] for f in flights))
    
    tk.Label(root, text="From:").pack()
    from_var = tk.StringVar()
    from_menu = ttk.Combobox(root, textvariable=from_var, values=locations)
    from_menu.pack()
    
    tk.Label(root, text="To:").pack()
    to_var = tk.StringVar()
    to_menu = ttk.Combobox(root, textvariable=to_var, values=locations)
    to_menu.pack()
    
    tk.Label(root, text="Date (DD/MM/YYYY):").pack()
    date_entry = tk.Entry(root)
    date_entry.pack()
    
    tk.Button(root, text="Search Flights", command=lambda: search_flights(root, from_var.get(), to_var.get(), date_entry.get())).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: CALLBACK_FUNCTION(root, CURR_USER)).pack(pady=5)

def search_flights(root, from_loc, to_loc, date):
    clear_widgets(root)
    tk.Label(root, text="Select your flight", font=("Arial", 14)).pack(pady=10)
    
    flights = [f for f in Flight.load_flights() if f["departure"] == from_loc and f["destination"] == to_loc and f["date"] == date]
    
    if not flights:
        tk.Label(root, text="No flights found!").pack()
        tk.Button(root, text="Back", command=lambda: find_flight(root, curr_user=CURR_USER, callback_function=CALLBACK_FUNCTION)).pack(pady=5)
        return
    
    selected_flight = tk.StringVar()
    for flight in flights:
        tk.Radiobutton(root, text=f"{flight['service_name']} - ₹{flight['price']} (Available Seats: {flight['availability']})", variable=selected_flight, value=flight["service_id"]).pack()
    
    tk.Label(root, text="Number of Seats:").pack()
    seats_entry = tk.Entry(root)
    seats_entry.pack()
    
    tk.Button(root, text="Book Flight", command=lambda: book_flight(root, selected_flight.get(), seats_entry.get())).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: find_flight(root, curr_user=CURR_USER, callback_function=CALLBACK_FUNCTION)).pack(pady=5)

def book_flight(root, flight_id, no_of_seats):
    try:
        no_of_seats = int(no_of_seats)
        flights = Flight.load_flights()
        
        for flight in flights:
            if str(flight["service_id"]) == flight_id:
                f_obj = Flight(flight["service_id"], flight["availability"], flight["price"], flight["service_name"], flight["departure"], flight["destination"], flight["date"])
                
                if f_obj.book_service(no_of_seats):
                    messagebox.showinfo("Success", "Flight booked successfully!")
                else:
                    messagebox.showerror("Error", "Not enough seats available!")
                
                find_flight(root, curr_user=None, callback_function=None)
                return
        
        messagebox.showerror("Error", "Flight not found!")
    except ValueError:
        messagebox.showerror("Error", "Invalid number of seats!")

# def main(root=None):
#     if root is None:
#         root = tk.Tk()
#     else:
#         clear_widgets(root)
#     root.title("Flight Booking System")
#     root.minsize(400, 300)
    
#     tk.Button(root, text="Find a Flight", command=lambda: find_flight(root)).pack(pady=20)
#     root.mainloop()

# if __name__ == "__main__":
#     main()
