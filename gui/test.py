import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


top = tk.Tk()
top.geometry('200x100')


label = tk.Label(top, text="input")
label.grid(column=0, row=0)

var = tk.IntVar()
text = tk.Checkbutton(top,variable=var)
text.grid(column=1, row=0)


varD = tk.DoubleVar()
ent = tk.Entry(top, variable=varD)


startButton = tk.Button(top, text='print', command=lambda:print(varD.get()))
startButton.grid(row=1)



top.mainloop()

