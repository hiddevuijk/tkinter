""" tkintert program """
import tkinter as tk

def do_nothing():
    """ do nothing """
    print(" I've done nothing. ")


def main():
    """ main loop """

    root = tk.Tk()

    menu = tk.Menu(root)
    root.config(menu=menu)

    sub_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=sub_menu)
    sub_menu.add_command(label="New Project ...", command=do_nothing)
    sub_menu.add_command(label="New ...", command=do_nothing)
    sub_menu.add_separator()
    sub_menu.add_command(label="Exit", command=do_nothing)

    edit_menu = tk.Menu(menu)
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Redo", command=do_nothing)

    root.mainloop()


if __name__ == "__main__":
    main()
