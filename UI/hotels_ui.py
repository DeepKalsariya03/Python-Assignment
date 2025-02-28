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

def find_hotel(root, curr_user, callback_function=None): 
    global CURR_USER, CALLBACK_FUNCTION
    CURR_USER = curr_user
    if callback_function:  # Only update CALLBACK_FUNCTION if it's not None
        CALLBACK_FUNCTION = callback_function

    clear_widgets(root)
    tk.Label(root, text="Searching hotels...", font=("Arial", 14)).pack(pady=10)
    
    # flights = Flight.load_flights()
    # locations = sorted(set(f["departure"] for f in flights) | set(f["destination"] for f in flights))
    
    # tk.Label(root, text="From:").pack()
    # from_var = tk.StringVar()
    # from_menu = ttk.Combobox(root, textvariable=from_var, values=locations)
    # from_menu.pack()
    
    # tk.Label(root, text="To:").pack()
    # to_var = tk.StringVar()
    # to_menu = ttk.Combobox(root, textvariable=to_var, values=locations)
    # to_menu.pack()
    
    # tk.Label(root, text="Date (DD/MM/YYYY):").pack()
    # date_entry = tk.Entry(root)
    # date_entry.pack()
    
    # tk.Button(root, text="Search Flights", command=lambda: search_flights(root, from_var.get(), to_var.get(), date_entry.get())).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: CALLBACK_FUNCTION(root, CURR_USER)).pack(pady=5)
    pass