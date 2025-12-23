# unit 5 question 2 part 4
# ODE describing an object under free fall

import tkinter as tk
import numpy as np
from scipy.integrate import odeint
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pyplot as plt

def freeFallODE(state_variables, time):
    # x, v = state_variables
    # state vars: [position, velocity]
    d2ydt2 = [state_variables[1], g]
    return d2ydt2


# y: vertical position of object
y0 = [0,0] #x, v
# t: time
time = np.linspace(0,10,1000)
# g: gravity
g = -9.81
# d^2y/dt^2: acceleration of the object in the vertical direction
d2ydt2 = odeint(freeFallODE, y0, time)
position = d2ydt2[:,0]
velocity = d2ydt2[:,1]




# Create a 600x600 Tkinter window titled "Object in Free Fall ODE"
frame = tk.Tk()
frame.title('Object in Free Fall ODE')
frame.geometry("600x600")

# Create a figure using the Figure class from matplotlib
fig = Figure(figsize=(8,6), dpi=100)

# Plot the solution to the ODE on the figure
plot1 = fig.add_subplot()
plot1.plot(time, position, label='Position')
plt.xlabel("Time")
plt.ylabel("Position")
plt.title('Object in Free Fall ODE')
# plt.legend()
plt.grid(True)

# Embed the figure using canvas FigureCanvasTkAgg
# place the MPL figure in the TK Frame
canvas = FigureCanvasTkAgg(fig,master=frame)
canvas.draw()
canvas.get_tk_widget().pack() 

# Embed a toolbar using NavigationToolbar2Tk
toolbar = NavigationToolbar2Tk(canvas, frame)
toolbar.update()
canvas.get_tk_widget().pack() 

# Display the window
frame.mainloop()