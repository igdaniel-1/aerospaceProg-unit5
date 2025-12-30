# Unit 5 question 3 part 2
# Exercise 2: Rocketship Form with Sun Valley 🚀
# Objectives:
# Create a form titled "Rocketship Form" (dimensions 500px by 300px) using tkinter and the Sun Valley dark theme
# Create a custom style named "Padding.TLabel" that applies a top padding of 10px and bottom padding of 5px to all the Labels
# Create a label and input field for "Rocketship Name"
# Create a label and input field for "Rocketship Destination"
# Create a label and input field for "Rocketship Mass"
# Create a label to show the output
# Create a button titled "Blast Off" when clicked and outputs the inputted information. The output should look like the following:
# Falcon 9 is heading to the International Space Station and weighs 228000 kg!

import tkinter as tk
from tkinter import ttk
import sv_ttk

frame = tk.Tk()
frame.geometry('500x300')
header = frame.title("Rocketship Form")

style = ttk.Style()
style.configure('Padding.TLabel', padding=(0,10,0,5))

# name
# note the use of 'ttk' when creating the styled labels
name_label = ttk.Label(frame, text="Rocket Name:", style='Padding.TLabel')
name_label.pack()
name_input = tk.Entry(frame)
name_input.pack()

# destination
destination_label = ttk.Label(frame, text="Destination:")
destination_label.pack()
destination_input = tk.Entry(frame)
destination_input.pack()

# # mass
mass_label = ttk.Label(frame, text="Rocket Mass:")
mass_label.pack()
mass_input = tk.Entry(frame)
mass_input.pack()

# output function
def blastOff():
    name = name_input.get()
    destination = destination_input.get()
    mass = mass_input.get()

    result = f"{name} is heading to {destination} and weighs {mass} kg!"
    output_label.config(text=result)


button = tk.Button(frame, text="Blast Off!", command=blastOff)
button.pack()

# output
output_label = tk.Label(frame, text="")
output_label.pack()



frame.mainloop()
