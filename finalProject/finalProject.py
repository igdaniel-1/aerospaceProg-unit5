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

frame = tk.Tk()
frame.title("Satellite Trajectory Analysis")
frame.geometry('1200x800')








frame.mainloop()