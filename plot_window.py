import tkinter as tk

import matplotlib.pyplot as plt


class PlotWindow:

    def plot(self):
        for key, value in self.parent.data_window.checkbox_vars.items():
            if value.get() == 1:
                data = self.parent.data_window.data[key]
                plt.plot(data.x, data.y, label=key)
            plt.axhline(1,color="black")
                
        plt.legend()
        plt.show()

    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame

        tk.Button(frame, text="Plot", command=self.plot).pack()
        

