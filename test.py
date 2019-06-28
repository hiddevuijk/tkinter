import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


root = tk.Tk()
root.geometry('200x100')


var = tk.StringVar()

r1 = tk.Radiobutton(root, text="one", variable=var, value="one")
r1.pack()
r2 = tk.Radiobutton(root, text="two", variable=var, value="two")
r2.pack()
r3 = tk.Radiobutton(root, text="three", variable=var, value="three")
r3.pack()

tk.Button(root, text="print", command=lambda:print(var.get())).pack()


root.mainloop()

