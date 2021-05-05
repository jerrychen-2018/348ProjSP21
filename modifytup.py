import tkinter as tk
import mysql.connector
from tkinter import *

# Finished: Update functions for Student, Faculty, Course
# TODO: CourseSection, Building, Classroom, Club, Department, Dormitory


def connect():
    cnx = mysql.connector.connect(user='root', password='rohanjerrytroy',
                                  host='35.224.65.220',
                                  database='schoolsystem')
    return cnx


def modify_home(root):
    global temp_root
    temp_root = root
    for widget in root.winfo_children():
        widget.destroy()

    table_options = [
        "Student",
        "Faculty",
        "Course",
        "Course Section",
        "Dormitory",
        "Department",
        "Classroom",
        "Club",
        "Building"
    ]

    clicked = tk.StringVar()
    clicked.set("Select Table")
    drop = OptionMenu(root, clicked, *table_options).grid(row=2, column=5)
    myButton = tk.Button(root, text="Confirm Selection", command=lambda: change_page(clicked.get())).grid(row=2, column=6)

def student_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Please enter the current ID of the student to be updated:',
                        font=('calibre', 10, 'bold')).grid(row=1, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: update_student(id_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def update_student(id_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    id = id_var.get()
    if (id == ""):
        # TODO print message about valid args
        change_page("back")
    new_name_var = tk.StringVar()
    new_grade_var = tk.StringVar()
    new_gpa_var = tk.StringVar()
    new_dorm_var = tk.StringVar()
    new_class_var = tk.StringVar()
    new_advisor_var = tk.StringVar()

    name_label = tk.Label(temp_root, text='New Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)

    grade_label = tk.Label(temp_root, text='New Grade', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    grade_entry = tk.Entry(temp_root, textvariable=new_grade_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    gpa_label = tk.Label(temp_root, text='New GPA', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    gpa_entry = tk.Entry(temp_root, textvariable=new_gpa_var, font=('calibre', 10, 'normal')).grid(row=2, column=1)

    dorm_label = tk.Label(temp_root, text='New Dormitory', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    dorm_entry = tk.Entry(temp_root, textvariable=new_dorm_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    classification_label = tk.Label(temp_root, text='New Classification', font=('calibre', 10, 'bold')).grid(row=4, column=0)
    classification_entry = tk.Entry(temp_root, textvariable=new_class_var, font=('calibre', 10, 'normal')).grid(
        row=4, column=1)

    adviser_label = tk.Label(temp_root, text='New Advisor', font=('calibre', 10, 'bold')).grid(row=5, column=0)
    adviser_entry = tk.Entry(temp_root, textvariable=new_advisor_var, font=('calibre', 10, 'normal')).grid(row=5, column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=6, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_student_update(id, new_name_var, new_grade_var, new_gpa_var, new_dorm_var, new_class_var, new_advisor_var)).grid(row=7, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_student_update(id, new_name_var, new_grade_var, new_gpa_var, new_dorm_var, new_class_var, new_advisor_var):
    new_name = new_name_var.get()
    new_grade = new_grade_var.get()
    new_gpa = new_gpa_var.get()
    new_dorm = new_dorm_var.get()
    new_class = new_class_var.get()
    new_advisor = new_advisor_var.get()

    if (new_name == "" and new_grade == "" and new_gpa == "" and new_dorm == "" and new_class == "" and new_advisor == ""):
        # TODO print message about valid args
        change_page("back")
    else:
        cnx = connect()
        cursor = cnx.cursor()
        data = (new_name, new_grade, new_gpa, new_dorm, new_class, new_advisor, id)
        update = ("UPDATE Student "
                  "SET stu_name = %s, grade_level = %s, gpa = %s, dormitory_name = %s, classification = %s, advisor = %s "
                  "WHERE student_id = %s")
        cursor.execute(update, data)
        cnx.commit()
        cursor.close()
        cnx.close()

    new_name_var.set("")
    new_grade_var.set("")
    new_gpa_var.set("")
    new_dorm_var.set("")
    new_class_var.set("")
    new_advisor_var.set("")


def faculty_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Please enter the current ID of the faculty to be updated:',
                        font=('calibre', 10, 'bold')).grid(row=1, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: update_faculty(id_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def update_faculty(id_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    id = id_var.get()
    if (id == ""):
        # TODO print message about valid args
        change_page("back")
    new_name_var = tk.StringVar()
    new_dept_var = tk.StringVar()
    new_salary_var = tk.StringVar()
    new_phone_var = tk.StringVar()
    new_office_var = tk.StringVar()
    new_building_var = tk.StringVar()

    new_name_label = tk.Label(temp_root, text='New Name', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    new_dept_label = tk.Label(temp_root, text='New Department', font=('calibre', 10, 'bold')).grid(row=2, column=0)
    new_dept_entry = tk.Entry(temp_root, textvariable=new_dept_var, font=('calibre', 10, 'normal')).grid(row=2,
                                                                                                             column=1)
    new_salary_label = tk.Label(temp_root, text='New Salary', font=('calibre', 10, 'bold')).grid(row=3, column=0)
    new_salary_entry = tk.Entry(temp_root, textvariable=new_salary_var, font=('calibre', 10, 'normal')).grid(row=3, column=1)

    new_phone_label = tk.Label(temp_root, text='New Phone Number', font=('calibre', 10, 'bold')).grid(row=4, column=0)
    new_phone_entry = tk.Entry(temp_root, textvariable=new_phone_var, font=('calibre', 10, 'normal')).grid(row=4, column=1)

    new_office_label = tk.Label(temp_root, text='New Office', font=('calibre', 10, 'bold')).grid(row=5, column=0)
    new_office_entry = tk.Entry(temp_root, textvariable=new_office_var, font=('calibre', 10, 'normal')).grid(row=5, column=1)

    new_building_label = tk.Label(temp_root, text='New Building', font=('calibre', 10, 'bold')).grid(row=6, column=0)
    new_building_entry = tk.Entry(temp_root, textvariable=new_building_var, font=('calibre', 10, 'normal')).grid(row=6, column=1)
    desc_label = tk.Label(temp_root, text='(Need to include input for all attributes, even if they remain the same)',
                          font=('calibre', 10, 'normal')).grid(row=7, column=0)
    sub_btn = tk.Button(temp_root, text='Submit',
                        command=lambda: commit_faculty_update(id, new_name_var, new_dept_var, new_salary_var, new_phone_var, new_office_var, new_building_var)).grid(row=7, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_faculty_update(id, new_name_var, new_dept_var, new_salary_var, new_phone_var, new_office_var, new_building_var):
    new_name = new_name_var.get()
    new_dept = new_dept_var.get()
    new_salary = new_salary_var.get()
    new_phone = new_phone_var.get()
    new_office = new_office_var.get()
    new_building = new_building_var.get()
    if (new_name == "" and new_dept == "" and new_salary == "" and new_phone == "" and new_office == "" and new_building == ""):
        # TODO print message about valid args
        change_page("back")
    cnx = connect()
    cursor = cnx.cursor()
    data = (new_name, new_dept, new_salary, new_phone, new_office, new_building, id)
    update = ("UPDATE Faculty "
              "SET faculty_name = %s, department = %s, salary = %s, phone_number = %s, office = %s, building = %s "
              "WHERE fac_id = %s")
    cursor.execute(update, data)
    cnx.commit()
    cursor.close()
    cnx.close()

    new_name_var.set("")
    new_dept_var.set("")
    new_salary_var.set("")
    new_phone_var.set("")
    new_office_var.set("")
    new_building_var.set("")


def course_page(root):
    id_var = tk.StringVar()

    id_label = tk.Label(root, text='Please enter the current ID of the course to be updated:', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    id_entry = tk.Entry(root, textvariable=id_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)

    sub_btn = tk.Button(root, text='Submit', command=lambda: update_course(id_var)).grid(row=2, column=1)
    back_btn = tk.Button(root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def update_course(id_var):
    for widget in temp_root.winfo_children():
        widget.destroy()
    id = id_var.get()
    if (id == ""):
        # TODO print message about valid args
        change_page("back")

    new_name_var = tk.StringVar()
    new_dept_var = tk.StringVar()

    new_name_label = tk.Label(temp_root, text='New Course Name', font=('calibre', 10, 'bold')).grid(row=0, column=0)
    new_name_entry = tk.Entry(temp_root, textvariable=new_name_var, font=('calibre', 10, 'normal')).grid(row=0, column=1)
    new_dept_label = tk.Label(temp_root, text='New Department', font=('calibre', 10, 'bold')).grid(row=1, column=0)
    new_dept_entry = tk.Entry(temp_root, textvariable=new_dept_var, font=('calibre', 10, 'normal')).grid(row=1, column=1)
    desc_label = tk.Label(temp_root, text='(Fields left blank will not modify the attribute)', font=('calibre', 10, 'normal')).grid(row=2, column=0)
    sub_btn = tk.Button(temp_root, text='Submit', command=lambda: commit_course_update(id, new_name_var, new_dept_var)).grid(row=2, column=1)
    back_btn = tk.Button(temp_root, text="Back", command=lambda: change_page("back")).grid(row=1, column=6)


def commit_course_update(id, new_name_var, new_dept_var):
    new_name = new_name_var.get()
    new_dept = new_dept_var.get()

    if (new_name == "" and new_dept == ""):
        # TODO print message about valid args
        change_page("back")
    else:
        cnx = connect()
        cursor = cnx.cursor()
        if (new_name == ""):
            data = (new_dept, id)
            update = ("UPDATE Course "
                      "SET department = %s "
                      "WHERE course_id = %s")
        elif (new_dept == ""):
            data = (new_name, id)
            update = ("UPDATE Course "
                      "SET course_name = %s "
                      "WHERE course_id = %s")
        else:
            data = (new_name, new_dept, id)
            update = ("UPDATE Course "
                      "SET course_name = %s, department = %s "
                      "WHERE course_id = %s")
        cursor.execute(update, data)
        cnx.commit()
        cursor.close()
        cnx.close()

    new_name_var.set("")
    new_dept_var.set("")


def change_page(table):
    for widget in temp_root.winfo_children():
        widget.destroy()
    if table == "back":
            modify_home(temp_root)
    elif table == "Student":
        student_page(temp_root)
    elif table == "Faculty":
        faculty_page(temp_root)
    elif table == "Course":
        course_page(temp_root)
    elif table == "Course Section":
        cs_page(temp_root)
    elif table == "Dormitory":
        dorm_page(temp_root)
    elif table == "Department":
        dept_page(temp_root)
    elif table == "Classroom":
        cr_page(temp_root)
    elif table == "Club":
        club_page(temp_root)
    elif table == "Building":
        b_page(temp_root)
