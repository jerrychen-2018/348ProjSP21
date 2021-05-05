import tkinter as tk
import mysql.connector
from tkinter import *



def connect():
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    return cnx

def reports_home(root):
    global temp_root
    temp_root = root
    for widget in root.winfo_children():
        widget.destroy()

    table_options = [
        "Student",
        "Faculty",
        "Course"
    ]

    clicked = tk.StringVar()
    clicked.set("Select Table")
    drop = OptionMenu(root, clicked, *table_options).grid(row=2, column=5)
    myButton = tk.Button(root, text="Confirm Selection", command=lambda: change_page(clicked.get())).grid(row=2, column=6)

def student_page(root):
        id_var = tk.StringVar()
        name_var = tk.StringVar()
        grade_var = tk.StringVar()
        gpa_var = tk.StringVar()
        dorm_var = tk.StringVar()
        classification_var = tk.StringVar()
        adviser_var = tk.StringVar()

        id_label = tk.Label(root, text='Student ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
        id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

        name_label = tk.Label(root, text='Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
        name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

        grade_label = tk.Label(root, text='Grade', font=('calibre', 10, 'bold')).grid(row=2, column=0)
        grade_entry = tk.Entry(root, textvariable=grade_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

        gpa_label = tk.Label(root, text='GPA', font=('calibre', 10, 'bold')).grid(row=3, column=0)
        gpa_entry = tk.Entry(root, textvariable=gpa_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

        dorm_label = tk.Label(root, text='Dormitory', font=('calibre', 10, 'bold')).grid(row=4, column=0)
        dorm_entry = tk.Entry(root, textvariable=dorm_var, font=('calibre', 10, 'normal')).grid(row=4, column=1)

        classification_label = tk.Label(root, text='Classification', font=('calibre', 10, 'bold')).grid(row=5, column=0)
        classification_entry = tk.Entry(root, textvariable=classification_var, font=('calibre', 10, 'normal')).grid(
            row=5, column=1)

        adviser_label = tk.Label(root, text='Advisor', font=('calibre', 10, 'bold')).grid(row=6, column=0)
        adviser_entry = tk.Entry(root, textvariable=adviser_var, font=('calibre', 10, 'normal')).grid(row=6, column=1)
        sub_btn = tk.Button(root, text='ADD', command=lambda: insert_student(id_var, name_var, grade_var, gpa_var, dorm_var, classification_var, adviser_var)).grid(row=7, column=1)
        back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)

def insert_student(id_var, name_var, grade_var, gpa_var, dorm_var, classification_var, adviser_var):
    id = id_var.get()
    name = name_var.get()
    grade = grade_var.get()
    gpa = gpa_var.get()
    dorm = dorm_var.get()
    classification = classification_var.get()
    adviser = adviser_var.get()

    if(id == "" or name == "" or grade == "" or gpa == "" or dorm == "" or classification == "" or adviser == ""):
        #TODO print message about valid args
        change_page("back")


    cnx = connect()
    cursor = cnx.cursor()
    student_data = (id, name, grade, gpa, dorm, classification, adviser)
    insertion = ("INSERT INTO Student "
                 "(student_id, stu_name, grade_level, gpa, dormitory_name, classification, advisor) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(insertion, student_data)
    cnx.commit()
    cursor.close()
    cnx.close()

    id_var.set("")
    name_var.set("")
    grade_var.set("")
    gpa_var.set("")
    dorm_var.set("")
    classification_var.set("")
    adviser_var.set("")

def faculty_page(root):
    id_var = tk.StringVar()
    name_var = tk.StringVar()
    salary_var = tk.StringVar()
    phone_var = tk.StringVar()

    id_label = tk.Label(root, text='Student ID', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    name_label = tk.Label(root, text='Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    salary_label = tk.Label(root, text='Salary', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    salary_entry = tk.Entry(root, textvariable=salary_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    phone_label = tk.Label(root, text='phone', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    phone_entry = tk.Entry(root, textvariable=phone_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    sub_btn = tk.Button(root, text='ADD',
                        command=lambda: insert_faculty(id_var, name_var, salary_var, phone_var).grid(row=7, column=1))
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=2, column=6)


def insert_faculty(id_var, name_var, salary_var, phone_var):
    id = id_var.get()
    name = name_var.get()
    salary = salary_var.get()
    phone = phone_var.get()
    if(id == "" or name == "" or salary == "" or phone == ""):
        #TODO print message about valid args
        change_page("back")


    cnx = connect()
    cursor = cnx.cursor()
    faculty_data = (id, name, salary, phone)
    insertion = ("INSERT INTO Facultly "
                 "(student_id, stu_name, grade_level, gpa, dormitory_name, classification, advisor)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    cursor.execute(insertion, faculty_data)
    cnx.commit()
    cursor.close()
    cnx.close()

    id_var.set("")
    name_var.set("")
    salary_var.set("")
    phone_var.set("")


def change_page(table):
    for widget in temp_root.winfo_children():
        widget.destroy()
    if table == "back":
            delete_home(temp_root)
    elif table == "Student":
        student_page(temp_root)
    elif table == "Faculty":
        faculty_page(temp_root)
    #elif table == "Course":
    #    course_page(temp_root)
