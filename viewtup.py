import tkinter as tk
import mysql.connector
from tkinter import *
import main
import inserttup as insert


def page1(root):
    for widget in root.winfo_children():
        widget.destroy()
    global temp_root
    temp_root = root
    tk.Label(root, text='view page').grid(row=0)
    tk.Button(temp_root, text='Home', command=lambda: main.home(temp_root)).grid(row=1, column=0)
    tk.Button(temp_root, text='Insert', command=lambda: insert.page1(temp_root)).grid(row=1, column=1)
    tk.Button(temp_root, text='View', command=lambda: page1(temp_root)).grid(row=1, column=2)
    tk.Button(temp_root, text='Execute query', command=lambda: get_stud(temp_root)).grid(row=2, column=1)


def get_stud(root):
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    cursor = cnx.cursor(buffered=True)
    cursor.execute("SELECT * FROM Faculty")
    res = cursor.fetchall()
    i = 3
    for x in res:
        lab = tk.Label(root, text=str(x), font=('calibre', 10, 'bold')).grid(row=i, column=3)
        i += 1
    cnx.commit()
    cursor.close()
    cnx.close()
