# unit 5 question 1 part 1
import tkinter as tk

# set up the framing
frame = tk.Tk()
frame.title("Input Form")

# label = tk.Label(text="hiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
# Organizes the label on the window 
# label.pack()

# sticky="e" means that the widget will stick to the east (right) edge of its grid cell
tk.Label(frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(frame, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

name_input = tk.Entry(frame)
name_input.grid(row=0, column=1, padx=10, pady=5)
age_input = tk.Entry(frame)
age_input.grid(row=1, column=1, padx=10, pady=5)

# submit input function
def print_info():
    input_values_label.config(text=f"Name: {name_input.get()}, Age: {age_input.get()}")

# submit button for input
tk.Button(frame, text="Submit", command=print_info).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Creating Dynamic Labels
input_values_label = tk.Label(frame, text="")
input_values_label.grid(row=3, column=0, columnspan=2)

# this command 'runs' the GUI
# Creates the main loop of the application which continuously listens for user input
frame.mainloop()