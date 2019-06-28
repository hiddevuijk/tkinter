""" tkinter program """
import tkinter as tk

import numerics_window as pw

class MasterWindow:
    """ the master frame """
    def __init__(self, master):
        self.master = master

        # Numerics window
        self.num_frame = tk.Frame(self.master, width=800, height=800)
        self.num_frame.grid(row=0, column=0)
        self.num_window = pw.NumWindow(self.num_frame)

        # Data window
        self.data_frame = tk.Frame(self.master, width=800, height=400)
        self.data_frame.grid(row=0, column=1)

        # Plot window
        self.plot_frame = tk.Frame(self.master, width=800, height=400)
        self.plot_frame.grid(row=1, column=1)

def main():
    """ main loop """

    root = tk.Tk()

    master_frame = MasterWindow(root)

    root.mainloop()


if __name__ == "__main__":
    main()
