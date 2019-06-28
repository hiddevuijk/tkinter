""" Numerics window class """
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


class Data:
    def __init__(self, x=[0], y=[0]):
        self.x = x
        self.y = y

class DataWindow:
    """ window for Data """

    def data2frame(self):
        """ Remove all  checkboxes, 
            and draw a checkbox for each data element """
        # delete all checkboxes
        for key, value in self.checkboxes.items():
            value.destroy()
        # clear dictionaries
        self.checkbox_vars.clear()
        self.checkboxes.clear()

        # put a checkbox on the frame for each data element
        for i, key in enumerate(self.data):
            if key is not "previous":
                self.checkbox_vars[key] = tk.IntVar()
                self.checkboxes[key] = tk.Checkbutton(self.frame, text=key, variable=self.checkbox_vars[key])
                self.checkboxes[key].grid(row=i, sticky="W") 

    def add_data(self, name, r, gr):
        """ add a data element to the data dict
            and put the corresponding checkboxes
            on the frame """
        self.data[name] = Data(r,gr)
        self.data2frame()
        

    def delete_data(self):
        """ Delete all selected data elements """
        deleted_keys = []
        for key, value in self.checkbox_vars.items():
            if value.get() == 1:
                deleted_keys.append(key)
                del self.data[key]
        
        # put a checkbox for each data element on the frame 
        self.data2frame()
            

    def __init__(self, parent, frame):
        """ initialize data frame """
        parent = parent
        self.frame = frame


        # all data elements saved from num. calculations
        self.data = {}
        # variables in checkboxes
        self.checkbox_vars = {} 
        # checkboxes on the frame for each data element
        self.checkboxes = {}

        # delete all selected data elements
        tk.Button(self.frame, text="Delete", command=self.delete_data).grid(row=100)
