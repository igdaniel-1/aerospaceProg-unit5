# unit 5 question 2 part 2

import tkinter as tk
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import numpy as np

# Create a 600x600 Tkinter window titled "Sin Graph using Tkinter"
frame = tk.Tk()
frame.title('Sin Graph using Tkinter')
frame.geometry("600x600")

# Create a figure using the Figure class from matplotlib
fig = Figure(figsize=(5,5), dpi=100)

# Plot np.sin(x) using the following: 
# x range = np.linspace(0, 2*np.pi, 100)
x = np.linspace(0, 2*np.pi, 100)
y = [np.sin(i) for i in x]

# y = y.astype(int)
print('10 y values:', y[:10])

plot1 = fig.add_subplot()
plot1.plot(x,y)

# Embed the figure using canvas FigureCanvasTkAgg
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Embed a toolbar using NavigationToolbar2Tk
toolbar = NavigationToolbar2Tk(canvas, frame)
canvas.get_tk_widget().pack()

# Display the window
frame.mainloop()