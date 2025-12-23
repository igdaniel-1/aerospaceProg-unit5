# unit 5 question 2 part 1
# plot the solution for the ODE of a harmonic oscillator

import tkinter as tk

import tkinter as tk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

frame = tk.Tk()
frame.title('ODE plotting')
frame.geometry("600x600")

fig = Figure(figsize=(5,5), dpi=100)
x = range(101)
y = [i ** 2 for i in x] #square everything in x

plot1 = fig.add_subplot(111)
plot1.plot(x, y)

# embed MPL figure in TK frame
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
# place canvas in the frame
canvas.get_tk_widget().pack() 

toolbar = NavigationToolbar2Tk(canvas, frame) 
toolbar.update() 
# Place toolbar in the frame 
canvas.get_tk_widget().pack()

# this command 'runs' the GUI
# Creates the main loop of the application which continuously listens for user input
frame.mainloop()