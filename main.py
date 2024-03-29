""" tkinter program """
import tkinter as tk

import numerics_window as nw
import data_window as dw
import sim_window as sw
import plot_window as pw

class MasterWindow:
    """ the master frame """
    def __init__(self, master):
        self.master = master

        # Numerics window
        self.num_frame = tk.Frame(self.master, width=100, height=100)
        self.num_frame.grid(row=0, column=0)

        self.num_window = nw.NumWindow(self, self.num_frame)

        # Data window
        self.data_frame = tk.Frame(self.master, width=100, height=100)
        self.data_frame.grid(row=0, column=1)
        self.data_window = dw.DataWindow(self, self.data_frame)

        # Plot window
        self.plot_frame = tk.Frame(self.master, width=100, height=100)
        self.plot_frame.grid(row=1, column=1)
        self.plot_window = pw.PlotWindow(self, self.plot_frame)

def main():
    """ main loop """

    root = tk.Tk()

    master_frame = MasterWindow(root)

    root.mainloop()


if __name__ == "__main__":
    main()
