# Unit 5 question 3 part 1
# Objectives:
# Initialize a window using tkinter
# Add a Label component that states "Hello World"
# Add a Button component that says "Click Button"
# Set the theme to dark mode using sv_ttk
# Run the application

import tkinter
from tkinter import ttk
import sv_ttk

# root == frame
root = tkinter.Tk()
header = root.title("Header")


tkinter.Label(root, text="Hello World").grid(row=0, column=0, padx=10, pady=5)


button = tkinter.Button(root, text='Click Button').grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Set the theme to dark mode!
sv_ttk.set_theme("dark")

root.mainloop()