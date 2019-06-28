""" Numerics window class """
import tkinter as tk

from numerics import *

class TextWindow:
    """ Window with ouput text """
    def __init__(self, textframe):
        self.textframe = textframe
        self.textframe.config(state=tk.DISABLED)

    def add_line(self, line): 
        self.textframe.config(state=tk.NORMAL)
        self.textframe.insert(tk.END, line + "\n")
        self.textframe.yview_pickplace(tk.END)
        self.textframe.config(state=tk.DISABLED)



class NumWindow:
    """ window for numerics """

    def clear_text(self):
        self.text.config(state=tk.NORMAL)
        self.text.delete('1.0', tk.END)
        self.text.config(state=tk.DISABLED)

    def read_input(self):
        self.start_numerics.config(state=tk.NORMAL)
        self.stop_numerics = True
        self.text_window.add_line('-'*60)
        self.text_window.add_line('Read Input')
        self.text_window.add_line('-'*60)
        self.num_int.it = 0
        try:
            self.num_int.HS = self.hs_var.get()
        except:
            self.text_window.add_line("problem reading HS")

        try:
            temp = float(self.rho_entry.get())
            self.num_int.rho = temp
        except:
            self.text_window.add_line("problem reading rho")

        try:
            temp = float(self.T_entry.get())
            self.num_int.T = temp
        except: 
            self.text_window.add_line("problem reading T")

        try:
            temp = float(self.rco_entry.get())
            self.num_int.r_co = temp
        except: 
            self.text_window.add_line("problem reading r_co")

        try:
            temp = float(self.a_entry.get())
            self.num_int.a = temp
        except: 
            self.text_window.add_line("problem reading alpha")

        try:
            temp = float(self.R_entry.get())
            self.num_intRT = temp
        except: 
            self.text_window.add_line("problem reading R")

        try:
            temp = int(self.Nexp_entry.get())
            self.num_int.Nexp = temp
        except: 
            self.text_window.add_line("problem reading Nexp")

        try:
            temp = float(self.eps_conv_entry.get())
            self.num_int.eps_conv = temp
        except: 
            self.text_window.add_line("problem reading eps_conv")

        try:
            temp = int(self.max_it_entry.get())
            self.num_int.max_it = temp
        except: 
            self.text_window.add_line("problem reading max_it") 


    def set_stop_numerics(self, true_false):
        self.start_numerics.config(state=tk.NORMAL)
        self.stop_numerics = true_false

    def run_numerics(self):
        self.start_numerics.config(state=tk.DISABLED)
        if self.stop_numerics == False:
            if self.num_int.it == 0:
                ok = self.num_int.init_vectors()
                if  not ok:
                    self.text_window.add_line("N not equal to previous N")
            
            if self.num_int.it % self.num_int.print_every == 0:
                self.text_window.add_line(str(self.num_int.it)+'\t'+str(self.num_int.eps)+'\t'+str(self.num_int.eps_conv))

            if self.num_int.it > self.num_int.max_it:
                self.text_window.add_line("MAX IT reached")               
                self.stop_numerics = True
            if self.num_int.eps < self.num_int.eps_conv:
                self.text_window.add_line(str(self.num_int.eps))               
                self.text_window.add_line("eps reached")               
                self.stop_numerics = True

            self.num_int.iterate()
            self.frame.after(1,self.run_numerics)
        else:
            self.start_numerics.config(state=tk.NORMAL)
            self.stop_numerics = False

    def __init__(self, frame):
        self.frame = frame

        self.stop_numerics = False
        # Numerics Input
        self.hs_var = tk.IntVar()
        self.hs_label = tk.Label(frame, text="HS")
        self.hs_label.grid(row=1,column=0)
        self.hs_check = tk.Checkbutton(frame,variable=self.hs_var)
        self.hs_check.grid(row=1,column=1)
        
        self.rho_label = tk.Label(frame, text="rho")
        self.rho_label.grid(row=2, column=0)
        self.rho_entry = tk.Entry(frame) 
        self.rho_entry.grid(row=2, column=1)

        self.T_label = tk.Label(frame, text="T")
        self.T_label.grid(row=3, column=0)
        self.T_entry = tk.Entry(frame) 
        self.T_entry.grid(row=3, column=1)

        self.rco_label = tk.Label(frame, text="r_co")
        self.rco_label.grid(row=4, column=0)
        self.rco_entry = tk.Entry(frame) 
        self.rco_entry.grid(row=4, column=1)

        self.a_label = tk.Label(frame, text="alpha")
        self.a_label.grid(row=1, column=2)
        self.a_entry = tk.Entry(frame)
        self.a_entry.grid(row=1, column=3)

        self.R_label = tk.Label(frame, text="R_max")
        self.R_label.grid(row=2, column=2)
        self.R_entry = tk.Entry(frame)
        self.R_entry.grid(row=2, column=3)

        self.Nexp_label = tk.Label(frame, text="N_exp")
        self.Nexp_label.grid(row=3, column=2)
        self.Nexp_entry = tk.Entry(frame)
        self.Nexp_entry.grid(row=3, column=3)

        self.eps_conv_label = tk.Label(frame, text="eps_conv")
        self.eps_conv_label.grid(row=4, column=2)
        self.eps_conv_entry = tk.Entry(frame)
        self.eps_conv_entry.grid(row=4, column=3)

        self.max_it_label = tk.Label(frame, text="max it")
        self.max_it_label.grid(row=5, column=2)
        self.max_it_entry = tk.Entry(frame)
        self.max_it_entry.grid(row=5, column=3)


        nr = 10
        # text for ouput
        self.text = tk.Text(frame)
        self.text.grid(row=nr+1, columnspan=4)
        self.text_window = TextWindow(self.text)
        # Pause numerics
        self.stop_num_button = tk.Button(self.frame, text="Pause", command=lambda:self.set_stop_numerics(True))
        self.stop_num_button.grid(row=nr,column=2)
        # read inpu
        self.read_input_button = tk.Button(self.frame, text="Read Input", command=self.read_input)
        self.read_input_button.grid(row=nr,column=0)
        # numerics
        self.num_int = NumInt()
        self.start_numerics = tk.Button(self.frame, text="Start Numerics", command=self.run_numerics)
        self.start_numerics.grid(row=nr, column=1)
        # clear text screen
        self.clear_text = tk.Button(self.frame, text="clear screen",command=self.clear_text)
        self.clear_text.grid(row=nr, column=3)
   
