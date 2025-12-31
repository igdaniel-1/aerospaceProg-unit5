import tkinter as tk
from tkinter import ttk
# import sv_ttk

frame = tk.Tk()
frame.title("S")
frame.geometry('500x200')

# print('whats good') 

slider = tk.Scale(frame, from_=0, to=200, tickinterval=20, orient=tk.HORIZONTAL,length=400)
slider.set(40) #sets the default slider value
slider.pack()

# sv_ttk.set_theme('dark')
frame.mainloop()