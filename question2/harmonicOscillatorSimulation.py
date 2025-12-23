# unit 5 question 2 part 3
# solution for the ODE of a harmonic oscillator

# w: angular frequency
# t: time
# x: position of the oscillator
# d^2 x / dt^2: acceleration of the oscillator

import tkinter as tk
import numpy as np
from scipy.integrate import odeint
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pyplot as plt


### PART 1: DEFINE THE ODE 
# define ODE for harmonic oscillation
def harmonic_oscillator(y, t, omega):
    """
    Represents the equation of motion for a harmonic oscillator.
    y: [state variables] array-like, composed of position and velocity [x, v]
    t: [independent variable] float, time
    omega: [constants] float, angular frequency (related to the spring constant and mass)
    """
    x, v = y
    dydt = [v, -omega**2 * x]  # Equation of motion for a harmonic oscillator
    return dydt

### PART 2: SET PARAMETERS
# state variables
y0 = [1.0, 0.0]  # Initial conditions: position = 1, velocity = 0
# independent variable
time = np.linspace(0, 10, 1000)
# constants
omega = 2*np.pi  # Angular frequency (arbitrary value for demonstration)

# solution to harmonic osc ODE
dydt = odeint(harmonic_oscillator, y0, time, args=(omega,))
# Extract position and velocity from the solution
position = dydt[:, 0]
velocity = dydt[:, 1]


### PART 3: PLOTTING THE ODE
# set up frame
frame = tk.Tk()
frame.title('Simple Harmonic Oscillator Solution')
frame.geometry("600x600")

# define figure dimensions and scale against window size
fig = Figure(figsize = (8, 6), dpi = 100) 

plot1 = fig.add_subplot()
plot1.plot(time, position, label="Position")
plt.xlabel("Time")
plt.ylabel("Position")
plt.title('Position vs Time for Harmonic Oscillator')
plt.legend()
plt.grid(True)


### PART 4: EMBEDDING MPL PLOT INTO TKINTER CANVAS
# make canvas
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

# make toolbar
toolbar = NavigationToolbar2Tk(canvas, frame)
toolbar.update()
canvas.get_tk_widget().pack()

# display
frame.mainloop()