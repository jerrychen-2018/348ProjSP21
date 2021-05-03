import inserttup as insert
import tkinter as tk


def main():
    root = tk.Tk()
    width = 1000
    height = 1000
    root.geometry("%dx%d" % (width, height))
    root.title("School System 348")
    insert.page1(root)

    root.mainloop()

if __name__ == '__main__':
    main()