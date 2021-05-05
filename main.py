import inserttup as insert
import modifytup as modify
import deletetup as delete
import querytup as query
import reportstup as reports
import viewtup as view
import tkinter as tk


def main():
    root = tk.Tk()
    width = 1000
    height = 1000
    root.geometry("%dx%d" % (width, height))
    root.title("School System 348")
    home(root)
    root.mainloop()


def home(r):
    for widget in r.winfo_children():
        widget.destroy()
    tk.Button(r, text='Home', command=lambda: home(r)).grid(row=1, column=0)
    tk.Button(r, text='Insert', command=lambda: insert.insert_home(r)).grid(row=1, column=1)
    tk.Button(r, text='Query', command=lambda: query.query_home(r)).grid(row=1, column=2)
    tk.Button(r, text='Modify', command=lambda: modify.modify_home(r)).grid(row=1, column=3)
    tk.Button(r, text='Delete', command=lambda: delete.delete_home(r)).grid(row=1, column=4)
    #tk.Button(r, text='Reports', command=lambda: reports.reports_home(r)).grid(row=1, column=5)


if __name__ == '__main__':
    main()