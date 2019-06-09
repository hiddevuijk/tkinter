""" tkintert program """
import tkinter as tk
from tkinter import messagebox

def main():
    """ main loop """

    root = tk.Tk()

    answer = messagebox.askquestion("Question 1", "Do you like this?")
    if answer == 'yes':
        print(10_00)

    root.mainloop()


if __name__ == "__main__":
    main()
