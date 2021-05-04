import inserttup as insert
import viewtup as view
import tkinter as tk


def main():
    root = tk.Tk()
    width = 1000
    height = 1000
    root.geometry("%dx%d" % (width, height))
    root.title("School System 348")
    home(root)
    #insert.page1(root)

    root.mainloop()


def home(r):
    for widget in r.winfo_children():
        widget.destroy()
    tk.Button(r, text='Home', command=lambda: home(r)).grid(row=1, column=0)
    tk.Button(r, text='Insert', command=lambda: insert.page1(r)).grid(row=1, column=1)
    tk.Button(r, text='View', command=lambda: view.page1(r)).grid(row=1, column=2)

if __name__ == '__main__':
    main()