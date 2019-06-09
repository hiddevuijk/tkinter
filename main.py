""" tkintert program """
import tkinter as tk

def print_name(event):
    """ prints name """
    print("My name is Hidde.")


def main():
    """ main loop """

    root = tk.Tk()

    button_1 = tk.Button(root, text="Print Name")
    button_1.bind("<Button-1>", print_name)
    button_1.pack()


    root.mainloop()


if __name__ == "__main__":
    main()
