""" Numerics window class """
import tkinter as tk
import matplotlib.pyplot as plt
from numerics import * 
class TextWindow:
    """ Window with ouput text """
    def __init__(self, textframe):
        self.textframe = textframe
        self.textframe.config(state=tk.DISABLED)
        self.textframe.config(font=("Helvetica", 10))

    def add_line(self, line): 
        self.textframe.config(state=tk.NORMAL)
        self.textframe.insert(tk.END, line + "\n")
        self.textframe.yview_pickplace(tk.END)
        self.textframe.config(state=tk.DISABLED)



class NumWindow:
    """ window for numerics """

    def plot(self):
        self.num_int.calculate_hcd()
        
        plt.plot(self.num_int.r, self.num_int.d, label='d(r)')
        plt.plot(self.num_int.r, self.num_int.h, label='h(r)')
        plt.plot(self.num_int.r, self.num_int.c, label='c(r)')
        plt.axhline(0,color='black', ls=":")
        plt.legend()
        plt.show()
        
    def save_data(self):
        self.num_int.calculate_hcd()

        window = tk.Toplevel(self.frame)
        name_entry = tk.Entry(window)
        name_entry.pack()
        def save_close():
            self.parent.data_window.add_data(name_entry.get(),
                                             self.num_int.r,
                                             self.num_int.h+1)
            window.destroy()
        tk.Button(window, text="Save",
                  command=save_close).pack()


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

        if self.potential_var.get() == "HS":
            self.num_int.HS = 1
        elif self.potential_var.get() == "WCA":
            self.num_int.HS = 0
            self.num_int.r_co = 2**(1./6.)
        elif self.potential_var.get() == "LJ_sim":
            self.num_int.HS = 0
            self.num_int.r_co = 10. #????????
        elif self.potential_var.get() == "other":
            self.num_int.HS = 0
            try:
                temp = float(self.rco_entry.get())
                self.num_int.r_co = temp
            except: 
                self.text_window.add_line("problem reading r_co")
        

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
            temp = float(self.a_entry.get())
            self.num_int.a = temp
        except: 
            self.text_window.add_line("problem reading alpha")

        try:
            temp = float(self.R_entry.get())
            self.num_int.R = temp
        except: 
            self.text_window.add_line("problem reading R")

        try:
            temp = int(self.Nexp_entry.get())
            self.num_int.Nexp = temp
            self.num_int.N = -1+2**temp
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

        try:
            temp = int(self.print_every_entry.get())
            self.num_int.print_every = temp
        except:
            self.text_window.add_line("problem reading print n")


    def set_stop_numerics(self, true_false):
        self.start_numerics.config(state=tk.NORMAL)
        self.stop_numerics = true_false

    def run_numerics(self):
        self.start_numerics.config(state=tk.DISABLED)
        if self.stop_numerics == False:
            if self.num_int.it == 0:
                if self.use_prev_var.get() == 0:
                    self.num_int.init_vectors()
                else:
                    if self.num_int.N == len(self.num_int.rd):
                        self.text_window.add_line("used previous solution")
                        self.num_int.init_vectors_use_prev()
                    else:
                        self.text_window.add_line("N not equal to previous N")
                        return False
            
            elif self.num_int.it % self.num_int.print_every == 0:
                self.text_window.add_line(str(self.num_int.it)+'\t'+str(self.num_int.eps)+'\t'+str(self.num_int.eps_conv))

            elif self.num_int.it > self.num_int.max_it:
                self.num_int.rd_prev = self.num_int.rd
                self.text_window.add_line("MAX IT reached")               
                self.text_window.add_line(str(self.num_int.eps))               
                self.stop_numerics = True
                return True
            elif self.num_int.eps < self.num_int.eps_conv:
                self.num_int.rd_prev = self.num_int.rd
                self.text_window.add_line(str(self.num_int.eps))               
                self.text_window.add_line("eps reached")               
                self.text_window.add_line("iterations: "+str(self.num_int.it))
                self.stop_numerics = True
                return True

            self.num_int.iterate()
            self.frame.after(1,self.run_numerics)
        else:
            self.start_numerics.config(state=tk.NORMAL)
            self.stop_numerics = False

    def __init__(self, parent, frame):
        self.parent = parent
        self.frame = frame

        self.stop_numerics = False

        # Numerics Input
        self.potential_var = tk.StringVar()
        tk.Radiobutton(self.frame, text="HS", variable=self.potential_var, value="HS").grid(row=1,column=0)
        tk.Radiobutton(self.frame, text="WCA", variable=self.potential_var, value="WCA").grid(row=1,column=1)
        tk.Radiobutton(self.frame, text="LJ_sim", variable=self.potential_var, value="LJ_sim").grid(row=2,column=0)
        tk.Radiobutton(self.frame, text="other", variable=self.potential_var, value="other").grid(row=2,column=1)
        
        
        tk.Label(frame, text="rho").grid(row=4, column=0)
        self.rho_entry = tk.Entry(frame) 
        self.rho_entry.grid(row=4, column=1)

        tk.Label(frame, text="T").grid(row=5, column=0)
        self.T_entry = tk.Entry(frame) 
        self.T_entry.grid(row=5, column=1)

        tk.Label(frame, text="r_co").grid(row=3, column=0)
        self.rco_entry = tk.Entry(frame) 
        self.rco_entry.grid(row=3, column=1)

        self.use_prev_var = tk.IntVar()
        tk.Checkbutton(frame, text="use previous", variable=self.use_prev_var).grid(row=6,column=0)

        tk.Label(frame, text="alpha").grid(row=1, column=2)
        self.a_entry = tk.Entry(frame)
        self.a_entry.grid(row=1, column=3)

        tk.Label(frame, text="R_max").grid(row=2, column=2)
        self.R_entry = tk.Entry(frame)
        self.R_entry.grid(row=2, column=3)

        tk.Label(frame, text="N_exp").grid(row=3, column=2)
        self.Nexp_entry = tk.Entry(frame)
        self.Nexp_entry.grid(row=3, column=3)

        tk.Label(frame, text="eps_conv").grid(row=4, column=2)
        self.eps_conv_entry = tk.Entry(frame)
        self.eps_conv_entry.grid(row=4, column=3)

        tk.Label(frame, text="print n").grid(row=5, column=2)
        self.print_every_entry = tk.Entry(frame)
        self.print_every_entry.grid(row=5, column=3)

        tk.Label(frame, text="max it").grid(row=6, column=2)
        self.max_it_entry = tk.Entry(frame)
        self.max_it_entry.grid(row=6, column=3)


        nr = 10
        # text for ouput
        self.text = tk.Text(frame)
        self.text.grid(row=nr+1, columnspan=6)
        self.text_window = TextWindow(self.text)
        # Pause numerics
        self.stop_num_button = tk.Button(self.frame, text="Pause", command=lambda:self.set_stop_numerics(True))
        self.stop_num_button.grid(row=nr,column=2)
        # read input
        self.read_input_button = tk.Button(self.frame, text="Read Input", command=self.read_input)
        self.read_input_button.grid(row=nr,column=0)
        # numerics
        self.num_int = NumInt()
        self.start_numerics = tk.Button(self.frame, text="Start Numerics", command=self.run_numerics)
        self.start_numerics.grid(row=nr, column=1)
        # clear text screen
        self.clear_text = tk.Button(self.frame, text="clear screen",command=self.clear_text)
        self.clear_text.grid(row=nr, column=3)

        # save data
        self.save_data = tk.Button(self.frame, text="Save", command=self.save_data)
        self.save_data.grid(row=nr, column=4)
   
        # plot data
        self.plot_data = tk.Button(self.frame, text="Plot", command=self.plot)
        self.plot_data.grid(row=nr, column=5)
