# Unit 5 question 4 part 2
# download json data using tinker UI
# Exercise 2: Export data inside a tkinter application
# Objectives
# Create a tkinter window with the Sun Valley theme
# Create a button titled "Download JSON"
# When the button is clicked, save rockets into a JSON file titled rockets.json
# Display the window

import tkinter as tk
import json
from tkinter import ttk
import sv_ttk

rocketData = [
    {
        'name':'A',
        'number':'1'
    },
    {
        'name':'B',
        'number':'2'
    }
]

def submit():
    with open("question4-StoringJSON-CSV/rockets.json","w") as file:
        json.dump(rocketData, file)


frame = tk.Tk()
frame.title("Download JSON Data")
sv_ttk.set_theme("dark")

button = tk.Button(frame,text="Download JSON", command=submit)
button.pack()
frame.mainloop()

