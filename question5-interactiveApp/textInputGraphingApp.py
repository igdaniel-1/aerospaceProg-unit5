import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import csv

frame = tk.Tk()
frame.title("Line Plotter")
frame.geometry('500x800')

headerLabel = tk.Label(frame, text="Line Grapher with Text Input")
headerLabel.pack()

inputLabel = tk.Label(frame, text="Slope Value:")
inputLabel.pack()
slopeInput = tk.Entry(frame)
slopeInput.pack()

resolutionLabel = tk.Label(frame, text="Number of X Values:")
resolutionLabel.pack()
resolutionInput = tk.Entry(frame)
resolutionInput.pack() 

# empty mpl and tkinter canvases
matplotfigure = Figure(figsize = (8,6), dpi=100)
canvas = FigureCanvasTkAgg(matplotfigure, master=frame)

# plot data from slider input
def generatePlot(canvas, figure):
    if figure:
        figure.clear()
    
    slope = slopeInput.get()
    resolution = resolutionInput.get()

    if resolution:
        resolution = int(resolution)
        slope = int(slope)
        print('resolution:',resolution)
        print('slope::::',slope)

        # x = np.linspace(0, 10, resolution)
        x = [x for x in range(resolution)]
        y = [0]*resolution

        for x_value in range(len(x)):
            y[x_value] = slope * x_value
        
        subplot = figure.add_subplot()
        subplot.plot(x, y)
        canvas.draw()
    else:
        print('resolution required before graphing...')

plottingButton = tk.Button(frame, text="Generate Plot", command=lambda:generatePlot(canvas, matplotfigure))
plottingButton.pack()

# download x,y values as see in grpah and adjusted from the slider
def downloadGraph():
    slope = slopeInput.get()
    resolution = resolutionInput.get()

    if resolution:
        resolution = int(resolution)
        x = np.linspace(0,10,resolution)
        y = [0]*resolution
        with open('question5-interactiveApp/slopeData.csv','w',newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['x','y'])
            writer.writeheader()
            for x_value in range(len(x)):
                y[x_value] = slope * int(x_value)
                writer.writerow({'x':x[x_value], 'y':y[x_value]})

downloadButton = tk.Button(frame, text="Download Data (.csv)", command=downloadGraph)
downloadButton.pack()

canvas.get_tk_widget().pack()
generatePlot(canvas, matplotfigure)
frame.mainloop()