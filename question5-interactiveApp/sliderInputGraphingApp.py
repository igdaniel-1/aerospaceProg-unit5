import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

frame = tk.Tk()
frame.title("Sin Plotter")
frame.geometry('500x800')

headerLabel = tk.Label(frame, text="Sin Grapher with Custom Slider")
headerLabel.pack()

# input slider
amplitudeSlider = tk.Scale(frame, from_=0, to=20, tickinterval=1, orient=tk.HORIZONTAL,length=400)
amplitudeSlider.set(1) #sets the default slider value
amplitudeSlider.pack()
# empty mpl and tkinter canvases
matplotfigure = Figure(figsize = (8,6), dpi=100)
canvas = FigureCanvasTkAgg(matplotfigure, master=frame)

def generatePlot(canvas, figure):
    if figure:
        figure.clear()
    
    amplitude = amplitudeSlider.get()

    x = np.linspace(0, 10, 100)
    y = amplitude * np.sin(x)

    subplot = figure.add_subplot()
    subplot.plot(x, y)
    canvas.draw()

plottingButton = tk.Button(frame, text="Generate Plot", command=lambda:generatePlot(canvas, matplotfigure))
plottingButton.pack()

canvas.get_tk_widget().pack()
generatePlot(canvas, matplotfigure)
frame.mainloop()