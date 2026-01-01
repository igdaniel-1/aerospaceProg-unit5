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

inputLabel = tk.Label(frame, text="Text Input:")
inputLabel.pack()
slopeInput = tk.Entry(frame)
slopeInput.pack()
# empty mpl and tkinter canvases
matplotfigure = Figure(figsize = (8,6), dpi=100)
canvas = FigureCanvasTkAgg(matplotfigure, master=frame)

# plot data from slider input
def generatePlot(canvas, figure):
    if figure:
        figure.clear()
    
    slope = slopeInput.get()

    # x = np.linspace(0, 10, 100)
    x = np.linspace(0, 10, 10)

    # y = lambda: slope * x
    y = [0]*10
    # print("\nX:",x)

    for x_value in range(len(x)):
        # print('\nx_value:',int(x_value))
        # print('vnslkdvnsldvsldnv:',y[int(x_value)])
        y[x_value] = slope * x_value
    
    print('\nx',x)
    print("y",y)
    
    subplot = figure.add_subplot()
    subplot.plot(x, y)
    canvas.draw()

plottingButton = tk.Button(frame, text="Generate Plot", command=lambda:generatePlot(canvas, matplotfigure))
plottingButton.pack()

# # download x,y values as see in grpah and adjusted from the slider
# def downloadGraph():
#     # amplitude = amplitudeSlider.get()
#     x = np.linspace(0,10,100)
#     with open('question5-interactiveApp/slopeData.csv','w',newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=['x','y'])
#         writer.writeheader()

#         for x_value in range(len(x)):
#             y = amplitude * np.sin(x[x_value])
#             writer.writerow({'x':x[x_value], 'y':y})

# downloadButton = tk.Button(frame, text="Download Data (.csv)", command=downloadGraph)
# downloadButton.pack()

canvas.get_tk_widget().pack()
generatePlot(canvas, matplotfigure)
frame.mainloop()