# Tk window to add services.
import tkinter as tk
from tkinter import messagebox, ttk

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.Flights import Flight  

# To clear existing widgets
def clear_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def add_flight(root):
    clear_widgets(root)

    tk.Label(root, text="Add Flight Service", font=("Arial", 14)).pack(pady=10)
    
    tk.Label(root, text="Service ID:").pack()
    entry_service_id = tk.Entry(root)
    entry_service_id.pack()

    tk.Label(root, text="Availability:").pack()
    entry_availability = tk.Entry(root)
    entry_availability.pack()

    tk.Label(root, text="Price:").pack()
    entry_price = tk.Entry(root)
    entry_price.pack()

    tk.Label(root, text="Service Name:").pack()
    entry_service_name = tk.Entry(root)
    entry_service_name.pack()

    tk.Label(root, text="Departure:").pack()
    entry_departure = tk.Entry(root)
    entry_departure.pack()

    tk.Label(root, text="Destination:").pack()
    entry_destination = tk.Entry(root)
    entry_destination.pack()

    tk.Label(root, text="Date (DD/MM/YYYY):").pack()
    entry_date = tk.Entry(root)
    entry_date.pack()
    
    def save_flight():
        try:
            service_id = int(entry_service_id.get())
            availability = int(entry_availability.get())
            price = int(entry_price.get())
            service_name = entry_service_name.get()
            departure = entry_departure.get()
            destination = entry_destination.get()
            date = entry_date.get()
            
            Flight(service_id, availability, price, service_name, departure, destination, date)
            messagebox.showinfo("Success", "Flight created successfully!")
            main(root)  # Return to main menu
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter correct values.")
    
    tk.Button(root, text="Save Flight", command=save_flight).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: main(root)).pack(pady=5)

def add_hotel(root):
    clear_widgets(root)
    tk.Label(root, text="Hotel Service Under Development").pack()
    tk.Button(root, text="Back", command=lambda: main(root)).pack()

def add_package(root):
    clear_widgets(root)
    tk.Label(root, text="Package Service Under Development").pack()
    tk.Button(root, text="Back", command=lambda: main(root)).pack()

def main(root=None):
    if root is None:
        root = tk.Tk()  # Initialize Tkinter only once
    else:
        clear_widgets(root)  # Clear widgets to reuse the same window
    
    root.title("Add Travel Service")
    root.minsize(300, 200)

    tk.Button(root, text="Add Flight Service", command=lambda: add_flight(root)).pack()
    tk.Button(root, text="Add Hotel Service", command=lambda: add_hotel(root)).pack()
    tk.Button(root, text="Add Package Service", command=lambda: add_package(root)).pack()

    root.mainloop()

if __name__ == "__main__":
    main()
