# unit 5 question 1 part 2
# GUI calculator


# Objectives
# Create a Tkinter window display using the tkinter library
# Add text onto the window display stating "Addition Calculator"
# Add two inputs onto the window and store the inputs into variables number1 and number2 respectively
# Create a button titled "Add"
# Create a Label on the window that shows the sum of number1 and number2 when the Add button is clicked
# Display the window


import tkinter as tk

# set up the framing
frame = tk.Tk()
frame.title("Addition Calculator")

# input labels
tk.Label(frame, text="Number1:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(frame, text="Number2:").grid(row=1, column=0, padx=10, pady=5)

# inputs 
number1 = tk.Entry(frame)
number1.grid(row=0, column=1, padx=10, pady=5)
number2 = tk.Entry(frame)
number2.grid(row=1, column=1, padx=10, pady=5)

# output label, under the add button
output_label = tk.Label(frame, text="")
output_label.grid(row=3, column=0, columnspan=2,)

# calculate
def addCalculator():
    total = int(number1.get())+int(number2.get())
    output_label.config(text=f"{total}")

# addition button
tk.Button(frame, text="Add", command=addCalculator).grid(row=2, column=0, columnspan=2, padx=10, pady=5)


frame.mainloop()
