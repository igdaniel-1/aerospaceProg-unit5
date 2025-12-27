# Unit 5 question 3 part 1

import tkinter as tk
from tkinter import ttk
import sv_ttk

# root == frame
root = tk.Tk()
root.geometry('500x300')
header = root.title("User Form")


# tkinter.Label(root, text="Hello World").grid(row=0, column=0, padx=10, pady=5)
# button = tkinter.Button(root, text='Click Button').grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Set the theme to dark mode!
sv_ttk.set_theme("dark")

# Create a Style instance to make custom styles!
style = ttk.Style()
# Configure a class name called Margin.TLabel which shows a top padding of 10px when applied
style.configure('Margin.TLabel', padding=(0, 10, 0, 0))  # (left, top, right, bottom)

# create labels and input fields for the first name, last name, and email of the user
# the entry/input section MUST be declared before assigning to a grid location, FOR EXAMPLE:
# input = tk.Entry()
# input.grid()

tk.Label(root, text="First Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
fname_input = tk.Entry(root)
fname_input.grid(row=0, column=1, padx=10, pady=5, sticky="e")

tk.Label(root, text="Last Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
lname_input = tk.Entry(root)
lname_input.grid(row=1, column=1, padx=10, pady=5, sticky="e")

tk.Label(root, text="Email Address:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
email_input = tk.Entry(root)
email_input.grid(row=2, column=1, padx=10, pady=5, sticky="e")

def submit_form():
    fname = fname_input.get()
    lname = lname_input.get()
    email = email_input.get()

    user_data = f"First Name: {fname}, Last Name: {lname}, Email: {email}"
    submission = result_label.config(text=user_data)


submit_button = tk.Button(root, text="Submit Form", command=submit_form).grid(row=3, column=0, padx=10, pady=5, sticky="e")
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=1, padx=0, pady=0, sticky="e")

root.mainloop()