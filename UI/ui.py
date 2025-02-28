import tkinter as tk
from tkinter import messagebox
from tkinter import ttk, messagebox
from prettytable import PrettyTable
from tkcalendar import Calendar
from flights_ui import find_flight
from hotels_ui import find_hotel

# dictionary = {"username": "password"}
with open("Database/users.txt", "r") as db_file:
        data = db_file.read()
        dict_db = eval(data)

# To clear existing widgets
def clear_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def register(ui_username, ui_password, root):
    username = ui_username.get()
    password = ui_password.get()
    if username and password:
        if username in dict_db:
            messagebox.showerror("Error", "Username already exists!")
        else:
            dict_db[username] = password
            db_file = open("Database/users.txt", "w")
            db_file.write(str(dict_db))
            messagebox.showinfo("Success", "Registration successful!")
            print(f"User {username} have registered successfully!")
            
    else:
        messagebox.showerror("Error", "Please enter your details!")

def login(ui_username, ui_password, root):
    username = ui_username.get()
    password = ui_password.get()
    if username in dict_db and dict_db[username] == password:
        messagebox.showinfo("Success", "Login successful!")
        print(f"User {username} have logged in successfully!")
        show_travel_services(root, curr_user=username)
    else:
        messagebox.showerror("Error", "Invalid credentials!") 

def show_travel_services(root, curr_user):
    clear_widgets(root)

    tk.Label(root, text=f"Welcome {curr_user}! \nChoose an option:", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Book Flight", command=lambda: find_flight(root, curr_user, show_travel_services)).pack(pady=5)
    tk.Button(root, text="Book Hotel", command=lambda: find_hotel(root, curr_user, show_travel_services)).pack(pady=5)
    tk.Button(root, text="Book Package", command=lambda: messagebox.showinfo("Info", "Package booking not implemented")).pack(pady=5)


def main():
    root = tk.Tk()
    root.title("Travel Booking System")
    root.minsize(300, 200)

    tk.Label(root, text="Username:").pack()
    ui_username = tk.Entry(root)
    ui_username.pack()

    tk.Label(root, text="Password:").pack()
    ui_password = tk.Entry(root, show="*")
    ui_password.pack()

    tk.Button(root, text="Register", command=lambda: register(ui_username, ui_password, root)).pack()
    tk.Button(root, text="Login", command=lambda: login(ui_username, ui_password, root)).pack()

    root.mainloop()


if __name__ == "__main__":
    main()


