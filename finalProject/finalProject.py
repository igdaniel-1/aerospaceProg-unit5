# Unit 5 final project
# Project 5: Satellite Trajectory Analysis GUI 
# Objectives
# Understand the contextual background behind satellite trajectories
# Create a GUI using tkinter and matplotlib to plot satellite details
# Make the GUI interactive by adding numerical sliders and buttons
# Allow the user to download a CSV file including data for the project

import tkinter as tk
from tkinter import ttk
import sv_ttk
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
from PyAstronomy import pyasl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sgp4.api import Satrec
from sgp4.api import jday

# Create a tkinter window 
# titled "Satellite Trajectory Analysis" with dimensions of 1200x800
mainFrame = tk.Tk()
mainFrame.title("Satellite Trajectory Analysis")
mainFrame.geometry('1200x800')

# styling
# Set the tkinter theme to Sun Valley
sv_ttk.set_theme('dark')
# Set the matplotlib theme to dark_background
plt.style.use('dark_background')
# Create a tkinter Style instance
style = ttk.Style()
# Create a tkinter class titled Margin.TLabel with the styles: padding=(0, 20, 0, 5)
style.configure('Margin.TLabel', padding=(0, 20, 0, 5))
# Create a tkinter class titled TButton with the styles: padding=(10, 10), background="#000"
style.configure('TButton', padding=(10, 10), background="#000")

# create side-by-side frames
left_frame = tk.Frame(mainFrame, width=500, height=600)
left_frame.pack(side='left', fill='both', expand=True)
right_frame = tk.Frame(mainFrame, width=300, height=600)
right_frame.pack(side='right', fill='both', expand=True)


# creating the 6 input sliders for the keplarian elements
# label pack slider pack
semi_major_axis_label = ttk.Label(right_frame, text="Semi-Major Axis: ", style='Margin.TLabel')
semi_major_axis_label.pack()
semi_major_axis_slider = tk.Scale(right_frame, from_=2000, to=5000, tickinterval=10000, orient=tk.HORIZONTAL, length=400)
semi_major_axis_slider.pack()

eccentricity_label = ttk.Label(right_frame, text="Eccentricity: ", style='Margin.TLabel')
eccentricity_label.pack()
eccentricity_slider = tk.Scale(right_frame, from_=0, to=1, resolution=0.01, tickinterval=0.1, orient=tk.HORIZONTAL, length=400)
eccentricity_slider.pack()

inclination_label = ttk.Label(right_frame, text="Inclination: ", style='Margin.TLabel')
inclination_label.pack()
inclination_slider = tk.Scale(right_frame, from_=0, to=360, tickinterval=40, orient=tk.HORIZONTAL, length=400)
inclination_slider.pack()

raan_label = ttk.Label(right_frame, text="Right Ascension of Ascending Node: ", style='Margin.TLabel')
raan_label.pack()
raan_slider = tk.Scale(right_frame, from_=0, to=360, tickinterval=40, orient=tk.HORIZONTAL, length=400)
raan_slider.pack()

perigee_label = ttk.Label(right_frame, text="Argument of Perigee: ", style='Margin.TLabel')
perigee_label.pack()
perigee_slider = tk.Scale(right_frame, from_=1, to=360, tickinterval=40, orient=tk.HORIZONTAL, length=400)
perigee_slider.pack()

anomaly_label = ttk.Label(right_frame, text="Mean Anomaly: ", style='Margin.TLabel')
anomaly_label.pack()
anomaly_slider = tk.Scale(right_frame, from_=1, to=360, tickinterval=40, orient=tk.HORIZONTAL, length=400)
anomaly_slider.pack()


# Takes in six Keplarian Elements as parameters and sets the value to the sliders in the GUI
def display_sliders(a, e, i, o, w, v):
    semi_major_axis_slider.set(a)
    eccentricity_slider.set(e)
    inclination_slider.set(i)
    raan_slider.set(o)
    perigee_slider.set(w)
    anomaly_slider.set(v)
# Default:
# Semi-Major Axis: 10000
# Eccentricity: 0.1
# Inclination: 90
# RAAN: 40
# Argument of Periapsis: 1
# Mean Anamoly: 1
display_sliders(10000, 0.1, 90, 40, 1, 1)




mainFrame.mainloop()